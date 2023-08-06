# -*- coding: utf-8 -*-
#
# Copyright (c) 2016-2018 by Lars Klitzke, lars@klitzke-web.de
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

""" This module creates and manages tasks

This module is used by the easyched module for executing multiple
tasks in parallel. Therefore, the class Task represents one of
those tasks.

For an easier mangement of tasks, you can find a `Dispatcher`
which should be used to start, stop, pause, resume or kill tasks.

You can easily create a Task with
>>> task = Task(command='df', parameters='-h', queue=queue.ActionQueue())

and run it using
>>> task.start()

now should see the output of the executed program in the console

"""

import getpass
import logging
import os
import queue
import signal
import subprocess

from copy import copy
from enum import Enum
from multiprocessing import Queue
from multiprocessing.context import Process
from posix import setgid
from pwd import getpwnam
from threading import Thread, Event
from time import sleep

from easysched import state
from easysched.state import Action, Transition, Condition, Statemachine, NoNextStateAvailableError, NONESTATE
from easysched.tools.logging import initialize

IDLE = state.State("IDLE")

INITIALIZED = state.State("INITIALIZED")

RUNNING = state.State("RUNNING")

PAUSED = state.State("PAUSED")

TERMINATED = state.State("Terminated")


class Connection(object):
    """
    This class enables multi-channel interprocess communication.

    Use this class for passing information between two processes *P1* and *P2*
    using multiple channels. For a bidirectional communication you simply create
    an instance with two channels. The first channel can then be used for
    data from *P1* to *P2* and the second channel from *P2* back to *P1*.

    However, you can initialize a connection with three channels and its
    on your own how to interpret those channels.

    """

    class ConnectionAlreadyClosedError(RuntimeError):
        pass

    def __init__(self, channels=2):

        self.Queues = []

        for channel in range(channels):
            self.Queues.append(Queue())

    def put(self, data, channel):
        """
        Adds the given \a data to the \a channel

        Keyword Arguments:

            data:     Data to add
            channel:     Channel to add the data to

        Raises:

            IndexError: if the channel is not available
        """

        if data:
            try:
                self.Queues[channel.value].put(data)
            except AssertionError:
                raise Connection.ConnectionAlreadyClosedError()

    def get(self, channel, blocking=False):
        """
        Get data from \a channel blocking or non blocking

        Keyword Arguments:

            channel:     Channel to get the data from
            blocking:     Shall block or not

        Raises:

            IndexError: if the channel is not available
        """

        if blocking:
            return self.Queues[channel.value].get()
        else:
            return self.Queues[channel.value].get_nowait()

    def get_queue(self, channel):
        """
        Get a reference to the queue of \a channel

        Keyword Arguments:

            channel:     Channel to get the reference to

        Raises:

            IndexError if the channel is not available
        """
        return self.Queues[channel.value]

    def close(self, channel):
        """
        Closes the communication over the given channel

        Keyword Arguments:

            channel:     Channel to get the data from
        """
        self.Queues[channel].close()

    def close_all(self):
        """
        Closes all connections
        """

        for queue in self.Queues:
            logging.debug(
                'Close queue {} and wait until finished'.format(queue))
            try:
                queue.close()
            except OSError:
                pass

            queue.join_thread()

            logging.debug('finished')


class Channels(Enum):
    """
    Channels used by the tasks
    """
    RX = 0
    TX = 1
    Action = 2
    TaskInfo = 3
    Count = 4


class TaskNotAvailable(Exception):
    """
    Raise if a task is not available
    """
    pass


class TaskNotStoppedInTimeError(Exception):
    """
    Raise if the task does not stop in time
    """
    pass


class StoppableThread(Thread):
    """
    Base class for stoppable Threads

    In the run function or the function passed as target on initialization,
    you can check if the thread should stop by calling self._should_stop().

    If you want to implement a Thread which calls a Program and should wait
    until stop() is called by another Thread, you can call the _wait_for_stop()
    function which will block until stop() is called.

    """

    def __init__(
            self,
            *args,
            **kwargs):
        super().__init__(*args, **kwargs)

        self.Running = Event()

    def stop(self):
        """
        Indicates that the Thread should stop
        """

        self.Running.clear()

    def _should_stop(self):
        """
        Checks if the Thread should stop
        """
        return self.Running.is_set()

    def _wait_for_stop(self):
        """
        Wait until the Thread should stop

        @note: This will block the Thread until stop() is called
        """

        return self.Running.wait()


class HotWireThread(Thread):
    """
    This thread waits for incoming data on the HotWire connection

    If you want to stop that Thread you have to do two things in
    the correct order:

    1) Call the stop() function of the Thread
    2) Write 'kill' on the HotWire

    """

    def __init__(self, queue, notifier, name):
        """
        Initialize the Thread

        Keyword arguments:

            queue:     The HotWire queue
            notifier:  Function to notify if stop received
            name:      The name of the task this Thread belongs to

        """

        if name:
            super().__init__(name=str(name) + "::HotWire")
        else:
            super().__init__(name=name)

        self.HotWire = queue

        self.Data = None

        self.MessageAvailableEvent = Event()

        self.Notifier = notifier

        self.TaskName = name

    def run(self):

        logging.debug("Started")

        while True:
            try:
                data = self.HotWire.get()
            except EOFError:
                # this means that the connection was closed
                break
            except TypeError:
                # this means that the connection was closed
                break

            if data == "finished":
                logging.debug("Notify task {}".format(self.TaskName))
                self.Notifier(self.TaskName)
            elif data == "kill":
                break
            else:
                logging.debug("Received data {}".format(data))
                self.Data = data

                # indicate that the PID is available
                self.MessageAvailableEvent.set()

        logging.debug('Finished')

    def get_data(self):
        """
        Returns the internal data

        @note: Will block until data is available
        """

        # read data if available
        self.MessageAvailableEvent.wait()
        data = self.Data
        self.MessageAvailableEvent.clear()

        return data


class WaitForStateThread(StoppableThread):
    """
    Thread waiting for incoming state notification

    Here, it is used by the Information Process to asynchronously
    receive changes of a statemachine. Therefore, simply create
    a Queue the thread will listen from.

    >>> queue = multiprocessing.Queue()

    And pass it to the thread on creation

    >>> wait_thread = WaitForStateThread(queue)

    Now you can notify it with
    >>> Queue.put("IDLE")

    Afterwards, you can access the current state with

    >>> queue.get_state()
    IDLE

    Which will return the previously added state

    See the InformationRetrievalTask for an example
    """

    def __init__(self, queue, name=None):
        """
        Initialize the thread with the given \a queue

        Keywords arguments:

            queue:     Queue to listen from
            name:     Name of the Thread
        """

        super().__init__(name=name)

        self.State = None
        self.Queue = queue

    def run(self):

        logging.debug('Started')
        while not self._should_stop():

            state = self.Queue.get()

            if state == 'kill':
                logging.debug(
                    'Kill received. Will terminate.')
                break

            logging.debug('New state is {}'.format(state))
            self.State = state

        logging.debug("Finished")

    def get_state(self):
        """
        Returns the latest received task
        """
        return self.State


class InformationRetrievalTask(Process):
    """
    This class is the interface to the statemachine in order to query
    its current state. Due to the fact that the statemachine runs in
    a seperate process, another process is needed in order to get
    the current state of the task.

    On creation this class will register itself at the given
    statemachine in order to be notified if the state changes

    """

    def __init__(self, connection, statemachine):

        super().__init__(name=__class__)

        self.Connection = connection

        self.NotificationQueue = Queue()

        statemachine.register_notification(self.NotificationQueue)
        self.State = statemachine.get_state()

    def run(self):

        logging.info('Started')

        # create the thread which will handle incoming state changes
        # notification
        t = WaitForStateThread(
            queue=self.NotificationQueue,
            name="WaitForStateChangeThread")

        t.start()

        try:
            while True:

                logging.debug(" Wait for requests... ")
                item = self.Connection.get(Channels.TX, True)

                keywords = item.split(' ')

                logging.debug(
                    'Received info request {}'.format(item))

                if keywords[0] == 'state':

                    logging.debug('State {}'.format(t.State))

                    if len(keywords) > 1 and len(keywords[1]) > 0:
                        state = keywords[1]

                        Connection.put(data=t.State == state, channel=Channels.RX)
                    else:
                        self.Connection.put(t.State, Channels.RX)

                elif keywords[0] == 'kill':
                    self.NotificationQueue.put('kill')
                    break
                else:
                    self.Connection.put(None, Channels.RX)
        finally:
            logging.debug("Stop thread and wait")
            t.stop()

            t.join()

            logging.info('finished')


class Dispatcher(object):
    """
    This class manages `Task`s
    """

    def __init__(self):

        super().__init__()

        self.Tasks = {}

    def add(self, task):
        """
        Add the given `task`

        Keywords Arguments:

            task:     Task object
        """

        if task:
            name = task.get('Name')

            # initialize the dict for the new task
            self.Tasks[name] = {}

            self.Tasks[name]['Object'] = task

    def start(self, task):
        """
        Start the given \a task

        Keywords Arguments:

            task:     Task object
        """

        logging.debug('Going to start task {}'.format(task))

        task_obj = self._task(task)

        if "Instance" in task_obj:
            logging.debug('Task was already running. Kill it')
            # an instance is already runnung; kill it
            self.kill(task)

        task_obj["Instance"] = copy(task_obj["Object"])

        # Initialize the task
        logging.info('Initialize task')
        self._instance(task).init()

        task_obj['Connection'] = self._instance(task).get_connection()

        # start the task
        task_obj["Instance"].start()
        task_obj['Connection'].put("start", Channels.Action)

        # setup the HotWire Thread and wait for the PID
        task_obj['HotWire'] = HotWireThread(
            self._instance(task).HotWire,
            self._has_stopped_callback,
            task)

        task_obj['HotWire'].start()

        logging.debug('Get PID of task')

        task_obj['PID'] = self._hotwire(task).get_data()

        logging.debug('Task started')

    def pause(self, task):
        """
        Pauses the given \a task

        Keywords Arguments:

            task:     Task object
        """

        self._send_event(task, "pause")

    def resume(self, task):
        """
        Resumes the given \a task

        Keywords Arguments:

            task:     Task object
        """

        self._send_event(task, 'resume')

    def stop(self, task):
        """
        Stops the given \a task

        Keywords Arguments:

            task:     Task object
        """

        self._send_event(task, "stop")

    def kill(self, task):
        """
        Kills the given \a task

        Keywords Arguments:

            task:     Task object
        """

        logging.debug('Check if user process is running')

        if self._instance(task) and self._instance(task).is_alive():

            logging.debug('Still running. Will kill it')

            # terminate the process
            self._instance(task).terminate()

            # join blocked
            self._instance(task).join()

            # stop the hotwire thread
            self._stop_hotwire_thread(task)

            if self._pid(task):

                try:
                    os.kill(self._pid(task), 0)

                    # kill the process tree if available
                    os.killpg(os.getpgid(self._pid(task)), signal.SIGTERM)

                except ProcessLookupError:
                    # This arise if the task to kill do not exists
                    pass
                except OSError as err:
                    logging.info(
                        'The following exception was suppressed: {}',
                        err)
                    pass

            logging.debug('Wait for kill to apply')

        else:
            logging.debug('task already stopped')

        # close all communication channels to the task
        if self._connection(task):
            self._connection(task).close_all()

        if self._get_field_of_task('Connection', self._task(task)):
            del self._task(task)['Connection']

        if self._get_field_of_task('Instance', self._task(task)):
            del self._task(task)['Instance']

        if self._get_field_of_task('HotWire', self._task(task)):
            del self._task(task)['HotWire']

        logging.debug('Kill finished. Close the action queue.')

    def end(self, task):
        """
        Ends the task

        Keyword Arguments:

            task    Task to end

        @warning: Do not use this object after calling this function!
        """

        # self._hotwire(task).stop()

        self._object(task).end()
        self._del_task(task)

    def kill_all(self):
        """
        Kill all available tasks
        """

        for task in self.list_tasks():
            self.kill(task)

    def is_task(self, task):
        """
        Checks of the given task is a registered task

        Keyword arguments:

            task:    Task to check for

        Returns:

            True if the task is known. False otherwise
        """

        if task in self.Tasks:
            return True
        return False

    def list_tasks(self):
        """
        Returns a list of available tasks
        """

        retval = []

        for task in self.Tasks:
            retval.append(str(task))

        return retval

    def get_state(self, task):
        """
        Returns the state of the internal statemachine of \a task

        Keyword Arguments:

            task:     Task to retrieve the state from

        Raises:

                TaskNotAvailable: if the task does not exist
        """

        self._send_request(task, "state")

        return self._get_feedback(task)

    def join(self, task, timeout=None):
        """
        Waits for the task to stop

        Keyword Arguments:

            task:        Task top wait for
            timeout:     Time to wait

        Raises:

            TaskNotStoppedInTimeError: If the task has not stopped in time
        """
        self._instance(task).join(timeout)

        if self._instance(task).exitcode is None:
            raise TaskNotStoppedInTimeError()

    def _send_event(self, task, event):

        conn = self._connection(task)

        if conn:
            self._connection(task).put(event, Channels.Action)

    def _send_request(self, task, request):

        conn = self._connection(task)

        if conn:
            self._connection(task).put(request, Channels.TX)

    def _get_feedback(self, task):

        conn = self._connection(task)

        if conn:
            return self._connection(task).get(Channels.RX, True)
        else:
            return None

    def _stop_hotwire_thread(self, task):
        """
        Stops the HotWire Thread of the task

        Keyword Arguments:

            task:     Task to stop
        """

        self._instance(task).HotWire.put("kill")

    def _has_stopped_callback(self, task):
        """
        Callback function if task has stopped

        Keyword Arguments:

            task:    Task that stopped

        @note: Use this function for the HotWire Thread
        """
        conn = self._connection(task)

        if conn:
            conn.close_all()

    def _connection(self, task):
        """
        Returns the connection object of the given \a task

        Keyword Arguments:

            task:     Task to retrieve the instance from

        Raises:

            TaskNotAvailable: if the task does not exist
        """

        return self._get_field_of_task("Connection", self._task(task))

    def _instance(self, task):
        """
        Returns the instance object of the given \a task

        Keyword Arguments:

        task:     Task to retrieve the instance from

        Raises:

            TaskNotAvailable: if the task does not exist
        """

        return self._get_field_of_task("Instance", self._task(task))

    def _object(self, task):
        """
        Returns the original task object

        Keyword Arguments:

            task:     Name of the task to retrieve

        Raises:

            TaskNotAvailable: if the task does not exist
        """
        return self._get_field_of_task("Object", self._task(task))

    def _pid(self, task):
        """
        Returns the PID of the running user task

        Keyword Arguments:

            task:     Name of the task to retrieve the PID from

        Raises:

            TaskNotAvailable: if the task does not exist
        """
        return self._get_field_of_task("PID", self._task(task))

    def _hotwire(self, task):
        """
        Returns the HotWire thread handle of the task

        Keyword Arguments:

            task:     Name of the task

        Raises:

            TaskNotAvailable: if the task does not exist
        """
        return self._get_field_of_task("HotWire", self._task(task))

    def _get_field_of_task(self, field, task):
        """
        Returns the \a field from the \a task
        """

        if field in task:
            return task[field]
        else:
            return None

    def _del_task(self, task):
        """
        Deletes the task from the internal list

        Keyword Arguments:

            task:    Task to delete
        """

        if self.is_task(task):
            del self.Tasks[task]

    def _task(self, task):
        """
        Returns the task object of the given \a task

        Keyword Arguments:

            task:     Task to retrieve

        Raises:

                TaskNotAvailable: if the task does not exist
        """
        if not isinstance(task, str):
            task = str(task)

        if task in self.Tasks:
            return self.Tasks[task]
        else:
            raise TaskNotAvailable(
                'The task "{}" does not exist.'.format(task))


class Task(Process):
    """ Represents an executable system task."""

    _DEFAULT_INTERVAL = 0

    _DEFAULT_NICE = 19  # lowest priority on linux

    class UserIsUnknownError(RuntimeError):
        """ The user was not found on the system """
        pass

    class TaskIsUninitializedError(RuntimeError):
        """ The task is used but not initialized """
        pass

    def __init__(self, command, parameters, user=None, nice=_DEFAULT_NICE,
                 name=None, logfile=None, interval=_DEFAULT_INTERVAL):

        Process.__init__(self, name=name)

        self.Statemachine = None

        self.Connection = None

        self.InfoProcess = None


        self.params = {}
        self._set('Name', name.strip())
        self._set('Command', command.strip())
        self._set('Parameters', parameters)
        self._set('Interval', int(interval))
        self._set('Nice', nice)
        self._set('Logfile', logfile)
        self._set('User', user)
        self._set('PID', None)

        self.STM = {
            'START': IDLE,
            IDLE: [
                Transition(
                    Action('initialize', self._init),
                    Condition(name='just initialize', blocking=True),
                    INITIALIZED),
            ],

            INITIALIZED: [
                Transition(
                    Action('run', self._call),
                    Condition('start', blocking=True),
                    RUNNING),

                Transition(
                    Action('stop gracefully', self._stop),
                    Condition('stop', blocking=True),
                    NONESTATE),

            ],

            RUNNING: [
                Transition(
                    None,
                    Condition('pause', blocking=False),
                    PAUSED),

                Transition(
                    Action('stop gracefully', self._stop),
                    Condition('stop', blocking=False),
                    NONESTATE),

                Transition(
                    Action('run', self._call),
                    Condition(name='keep running'),
                    RUNNING,
                    int(self.get('Interval'))),
            ],

            PAUSED: [

                Transition(
                    Action('run', self._call),
                    Condition('resume', blocking=True),
                    RUNNING),

                Transition(
                    Action('stop gracefully', self._stop),
                    Condition('stop', blocking=True),
                    NONESTATE),
            ]
        }

        self.HotWire = Queue()

    def __repr__(self, *args, **kwargs):
        return self.get("Name")

    def init(self):
        """
        Initializes the Task
        """

        self.Connection = Connection(Channels.Count.value)

        self.Statemachine = Statemachine(
            self.STM,
            IDLE,
            self.Connection.get_queue(
                Channels.Action))

    def start(self, params=None):
        """
        Starts the Task
        """

        logging.debug('Start information retrieval task')
        self.InfoProcess = InformationRetrievalTask(self.Connection,
                                                    self.Statemachine)

        self.InfoProcess.start()

        logging.debug('Start user task')
        Process.start(self)

        logging.debug('Started')

    def get(self, param):
        """ Returns the specified param """
        return self.params[param]

    def get_connection(self):
        """
        Returned a Connection object in order to communicate with the Task
        """
        return self.Connection

    def terminate(self):
        """
        Terminate the Task if it does not stop
        """

        item = self.Connection.put('kill', Channels.TX)

        self.InfoProcess.join()

        Process.terminate(self)

        self.HotWire.put("finished")

    def run(self):
        """
        Calls the specified command as the specified user either once or cyclic
        """

        logging.info('Task {} started'.format(self.get('Name')))

        self._set('PID', os.getpid())

        # while True:
        try:
            while True:

                self.Statemachine.run()

                sleep(0.1)

        except NoNextStateAvailableError:
            logging.info('State machine finished')
        except Exception as err:
            logging.error(
                'An error occured while running the task: {}'.format(err), exc_info=1)

        logging.info('Stop information process')

        self.Connection.put('kill', Channels.TX)

        logging.debug('Task finished')

        self.HotWire.put("finished")

    def end(self):
        self.HotWire.close()

    def _set(self, name, param):
        self.params[name] = param

    def _init(self, params=None):
        """ Initialize the tasks """

        logfile = self.get('Logfile')

        if logfile:
            # try to open the file for writing
            try:
                self._set('Logfile', open(logfile, 'a'))
            except IOError as err:
                logging.warning(
                    'Error: %s. Cannot use log file %s', err, logfile)
                self._set('Logfile', None)

        user = self.get('User')

        if not user:
            # get the name of the user running this script
            user = getpass.getuser()

        try:
            self._set('User', getpwnam(user))
        except KeyError as err:
            raise Task.UserIsUnknownError(err)

    def _stop(self, params=None):

        # clean up the file
        if self.get('Logfile'):
            self.get('Logfile').close()

    def _call(self, params=None):
        """ Call the used defined program """

        # change the user id - will raise exceptions on errors, record it.
        try:
            setgid(self.get('User').pw_uid)
        except PermissionError as err:
            logging.error('Error %s: cannot change user id', err)

        # change the niceness -> priority of the process
        if self.get('Nice'):
            os.nice(int(self.get('Nice')))

        # setup named arguments
        args = {'shell': True}

        # append optional arguments for logging
        if self.get('Logfile'):
            args['stdout'] = self.get('Logfile')
            args['stderr'] = self.get('Logfile')

        # on the child, call setsid so that it will have its own group process
        # id. We use the process group id to terminate the process and the
        # bash instance which called the user program
        args['preexec_fn'] = os.setsid

        logging.info(
            'Run task {} {}'.format(
                self.get('Command'),
                self.get('Parameters')))

        # just run the process
        self.UserProcess = subprocess.Popen(
            "{} {}".format(self.get('Command'), self.get('Parameters')), **args)

        logging.debug(
            'User task is running at PID {}'.format(
                self.UserProcess.pid))

        logging.debug("Put PID on the HotWire")
        self.HotWire.put(self.UserProcess.pid)

        logging.debug("Wait for the Process to end")
        self.UserProcess.wait()


def create_tasks(config):
    """
    Create a list of tasks objects based on the passed configuration

    Keyword arguments:

        config -- Dictionary of task definitions

    This function will parses the given configuration and create a list of
    Task's for each entry in the configuration. You can then, use this list
    to call those tasks
    """
    tasks = []

    for entry in config:

        task = Task(**entry)

        tasks.append(task)

    return tasks


if __name__ == '__main__':
    initialize(level=logging.INFO, filename='test.log')

    t = Task(
        name='Test',
        command='date',
        parameters='+"%Y%m%d %H%M%S"',
        interval=1,
        logfile='test.log')

    d = Dispatcher()

    d.add(t)

    logging.info("Available tasks {}".format(d.list_tasks()))

    logging.info('Start')
    d.start(t)

    logging.info('current state %s', d.get_state(t))

    sleep(2)

    logging.info('Pause')
    d.pause(t)

    sleep(2)
    logging.info('current state %s', d.get_state(t))

    logging.info('Resume')
    d.resume(t)

    sleep(2)
    logging.info('current state %s', d.get_state(t))

    sleep(2)
    logging.info('current state %s', d.get_state(t))

    logging.info('Pause')
    d.pause(t)

    sleep(1)
    logging.info('current state %s', d.get_state(t))

    logging.info('Stop')
    d.stop(t)
    sleep(1)

    d.kill(t)

    logging.info('Restart process')
    d.start(t)

    logging.info('current state %s', d.get_state(t))
    sleep(2)

    logging.info('current state %s', d.get_state(t))
    sleep(1)
    logging.info('terminate process')

    d.kill(t)

    d.end(t)
