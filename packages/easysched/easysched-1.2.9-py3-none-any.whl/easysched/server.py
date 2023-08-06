#!/usr/bin/env python
#  -*- coding: utf-8 -*-
#
# This is the server of easysched - the config-based scheduler.
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

import argparse
import asyncio
import json
import logging
import os
import textwrap

from easysched.command import CMD_TASK_START, CMD_TASK_PAUSE, CMD_TASK_STOP, CMD_TASK_RESUME, CMD_TASK_KILL, \
    CMD_TASK_KILL_ALL, CMD_TASK_LIST, CMD_SYSTEM_EXIT, register, parse
from easysched.task import Connection, RUNNING, INITIALIZED, TaskNotStoppedInTimeError, TERMINATED, Dispatcher, \
    create_tasks
from easysched.tools import config
from easysched.tools.lock import lock, unlock
from easysched.tools.logging import initialize

MODULENAME = os.path.basename(__file__)

CONFIG_SECTION_BASE = 'easysched'

CONFIG_OPTION_LOG = 'log-dir'

CONFIG_OPTION_TMP = 'tmp-dir'

CONFIG_OPTION_TASK = 'Task-tag'

CONFIG_OPTION_PORT = 'port'

TMP_DIR = '/tmp/'

DEFAULT_PORT = 8400

EASYSCHED_DEAMON = "esdd"


class InvalidConfigurationError(RuntimeError):
    """ Error for an invalid configurations. """
    pass


def parse_arguments():
    """ Parses the program arguments"""

    arg_parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                         description="easysched is a Lightweight framework to easily "
                                                     "schedule multiple tasks.",
                                         epilog=textwrap.dedent("""
With this framework you can call every type of executable, independent
of the programming language, for instance bash/perl scripts, C/C++ programs,
Java... or any other executable. Additionally, you can define the priority of
a Task, which user should be the callee and if the Task should be run once or
cyclic by defining the Task execution interval and if the output of a process
should be logged into a file.                                        .

All of this is easily configurable with only one configuration file. The parse
process is based on the configparser class of python3.X with the extended
interpolation feature and enriched with additional functionality to call tasks.

===============================================================================

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
"""))
    arg_parser.add_argument('--config', help="""
        configuration file for fasva with details
        about the tasks to execute""", required=True)

    arg_parser.add_argument('--log-level', help="""
    defines which messages should be logged (INFO, DEBUG, WARNING, ERROR).
    For further modes see the logging class.
    """, default='WARNING', choices=['INFO', 'DEBUG', 'WARNING', 'ERROR'])

    return arg_parser.parse_args()


SUCCESS = {
    'code': 0
}

ERROR = {
    'code': 1
}


def list_tasks(dispatcher):
    logging.debug('Create list of tasks')

    result = SUCCESS
    states = []

    for task_ in dispatcher.list_tasks():
        logging.debug('Retrieve state of task %s', task_)
        try:
            state = dispatcher.get_state(task_)
        except Connection.ConnectionAlreadyClosedError:
            # Failed to retrieve the state.
            # This will occur if the task was stopped or killed
            # in that case, the connection to the task will be
            # destroyed and thus, accessing the queue will raise
            # the exception and you'll get here. Indicate this
            # by setting the state to TERMINATED
            state = TERMINATED

        logging.debug('State of task %s is %s', task_, str(state))
        states.append(
            "{task}\t{state}\n".format(task=task_, state=state)
        )

    result['value'] = "".join(states)

    return json.dumps(result)


def task_is_running(dispatcher, task):
    state = None

    try:
        state = dispatcher.get_state(task)
    except Connection.ConnectionAlreadyClosedError:
        pass

    if (state == RUNNING) or (
            state == INITIALIZED and state.transitioning):
        return True

    return False


def stop_wait_and_kill(dispatcher, task):
    if task and task_is_running(dispatcher, task):
        dispatcher.stop(task)

        logging.info("Wait for task {}".format(task))
        try:
            dispatcher.join(task, 5)
        except TaskNotStoppedInTimeError:
            logging.info("Task {} didn't stop in time. Kill it.".format(task))

            dispatcher.kill(task)

        logging.info("Now end the task")
        dispatcher.end(task)


def system_exit(dispatcher):
    global RUN

    logging.info('Shutdown easysched...')

    tasks = dispatcher.list_tasks()

    logging.debug('Stop all tasks and wait for them...')
    for task_ in tasks:
        stop_wait_and_kill(dispatcher, task_)

    RUN = False

    return json.dumps(SUCCESS)


# Global veriable to let easysched run
RUN = True


def init_commands(command_map):
    """ Initialize the command interpreter """

    for cmd in command_map:

        try:
            func, param = command_map[cmd]
        except ValueError:
            func = command_map[cmd][0]
            param = None

        logging.info('Add command "%s"', cmd)
        register(cmd, func, param)


def init():
    # parse arguments
    arguments = parse_arguments()

    # load the configuration
    configuration = config.load_configuration(arguments.config)

    if CONFIG_SECTION_BASE not in configuration:
        raise InvalidConfigurationError(
            'There is no section "{}" in the configuration'.format(CONFIG_SECTION_BASE))

    for opt in [CONFIG_OPTION_LOG, ]:
        if opt not in configuration[CONFIG_SECTION_BASE]:
            raise InvalidConfigurationError(
                'Option "{}" is missing in section "{}"'.format(
                    CONFIG_OPTION_LOG, CONFIG_SECTION_BASE))

    # create the directories defined in the configuratio    n
    config.create_directories(configuration)

    # initialize the logging module
    initialize(
        arguments.log_level,
        configuration[CONFIG_SECTION_BASE][CONFIG_OPTION_LOG] +
        os.sep +
        MODULENAME + ".log",
        "easysched")

    # get all task definition of the configuration file and register them at the dispatcher
    tasks = create_tasks(configuration['tasks'])

    dispatcher = Dispatcher()

    for task_ in tasks:
        logging.info("Add task %s", task_)
        dispatcher.add(task_)

    if CONFIG_OPTION_PORT in configuration[CONFIG_SECTION_BASE]:
        port = configuration[CONFIG_SECTION_BASE][CONFIG_OPTION_PORT]
    else:
        port = DEFAULT_PORT

    return dispatcher, port


async def server(host, port, dispatcher):
    """
    This is the 'main' coroutine everything is running in

    Args:
        host:   The host the server will run on
        port:   The port the server will listen on

    """

    # communication queue
    command_queue = asyncio.Queue()

    async def client_connected(reader, writer):
        """
        Client connected handler

        Args:
            reader (StreamReader):   Read data from the client
            writer (StremWriter):    Dend data to the client

        Returns:

        """

        # read in the command
        line = await reader.readline()

        line = line.decode()[:-1]
        # decode the line

        # check if the command is valid
        cmd, parameters = parse(line)

        logging.debug('Command {} received'.format(cmd))
        if not cmd:
            feedback = json.dumps(ERROR)

        # methods of the dispatcher cannot be called here due to the
        # fact that additional processes and threads may be spawned
        # inside this coroutine and thus, this thread will not end
        # until every spawned thread will finish. Hence, send all
        # dispatcher calls to the main coroutine. However, we cannot
        # retrieve the class a bound method belongs to and thus we
        # simply check if the function is a bound function and let
        # the main routine process it. This however has the negative
        # side effect that we cannot get the result of the function
        # and have to send a default message to the client.

        # check if cmd is a bound method - a bound method has the __self__ attribute
        elif hasattr(cmd.func, '__self__'):
            await command_queue.put((cmd, parameters))

            # wait for the main routine until it processed the command
            command_queue.join()

            feedback = json.dumps(SUCCESS)
        else:
            feedback = cmd.execute(*parameters)

        logging.debug('Send feedback "%s"', feedback)

        # the last line has to be empty - thus take care that the
        # feedback ends with two newlines
        feedback += "\n\n"

        writer.write(feedback.encode())

        await writer.drain()
        writer.write_eof()

        asyncio.sleep(1)
        writer.close()

        logging.debug('exit')

    # setup the dispatcher and bind the available commands to its methods
    command_map = {
        CMD_TASK_START: (dispatcher.start,),
        CMD_TASK_PAUSE: (dispatcher.pause,),
        CMD_TASK_STOP: (dispatcher.stop,),
        CMD_TASK_RESUME: (dispatcher.resume,),
        CMD_TASK_KILL: (dispatcher.kill,),
        CMD_TASK_KILL_ALL: (dispatcher.kill_all,),
        CMD_TASK_LIST: (list_tasks, dispatcher),
        CMD_SYSTEM_EXIT: (system_exit, dispatcher),
    }

    init_commands(command_map)

    # start the server - will call client_connected on each accepted connection
    srv = await asyncio.start_server(
        client_connected, host, port)

    while RUN:
        cmd, parameter = await command_queue.get()

        cmd.execute(*parameter)

        command_queue.task_done()

    # wait for the server to close
    await srv.wait_closed()


def main():
    """ Main routine of this module """

    easysched_lock = lock(
        os.path.join(
            TMP_DIR,
            MODULENAME))
    try:

        dispatcher, port = init()

        loop = asyncio.get_event_loop()
        loop.run_until_complete(server('127.0.0.1', port, dispatcher))
        loop.close()

    finally:
        unlock(easysched_lock)


if __name__ == '__main__':
    main()
