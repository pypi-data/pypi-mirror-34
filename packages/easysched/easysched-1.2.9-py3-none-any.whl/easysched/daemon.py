#!/usr/bin/env python
#  -*- coding: utf-8 -*-
# Copyright (c) 2016-2018 by Lars Klitzke, lars@klitzke-web.de
# All Rights Reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#
#    * Redistributions in binary form must reproduce the above
#      copyright notice, this list of conditions and the following
#      disclaimer in the documentation and/or other materials provided
#      with the distribution.
#
#    * Names of its contributors may be used to endorse or promote
#      products derived from this software without specific prior
#      written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# REGENTS OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
# OF THE POSSIBILITY OF SUCH DAMAGE.
""" This is the deamon of easysched

"""

import argparse
import logging
import os
import tempfile
import textwrap

from easysched import command
from easysched.command import add_command, parse_command
from easysched.task import TaskNotStoppedInTimeError, Dispatcher, create_tasks, Connection, INITIALIZED, RUNNING, \
    TERMINATED
from easysched.tools import Config
from easysched.tools.Lock import lock, unlock
from easysched.tools.Logging import initialize

# Name of this module which actually is the name of the file

MODULENAME = os.path.basename(__file__)

CONFIG_SECTION_BASE = 'easysched'

CONFIG_OPTION_LOG = 'log-dir'

CONFIG_OPTION_TMP = 'tmp-dir'

CONFIG_OPTION_TASK = 'Task-tag'

TMP_DIR = '/tmp/'

FIFO_RX = "easyschedrx"
FIFO_TX = "easyschedtx"

EASYSCHED_DEAMON = "esdd"


class InvalidConfigurationError(RuntimeError):
    """ Error for an invalid configurations. """
    pass


def parse_arguments():
    """ Parses the program arguments"""

    arg_parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                         description="""
                                        easysched -- """,
                                         epilog=textwrap.dedent("""'
    easysched is a Lightweight framework to easily schedule multiple tasks.

    With this framework you can call every type of executable, independent
    of the programming language, for instance bash/perl scripts, C/C++ programs,
    Java... or any other executable. Additionally, you can define the priority of
    a Task, which user should be the callee and if the Task should be run once or
    cyclic by defining the Task execution interval and if the output of a process
    should be logged into a file.                                        .

    All of this is easily configurable with only one configuration file. The parse
    process is based on the configparser class of python3.X with the extended
    interpolation feature and enriched with additional functionality to call tasks.
    """))

    arg_parser.add_argument('--config', help="""
        configuration file for fasva with details
        about the tasks to execute""", required=True)

    arg_parser.add_argument('--log-level', help="""
    defines which messages should be logged (INFO, DEBUG, WARNING, ERROR).
    For further modes see the logging class.
    """, default='WARNING', choices=['INFO', 'DEBUG', 'WARNING', 'ERROR'])

    return arg_parser.parse_args()


def read_fifo(fifo):
    while True:
        with open(fifo) as piperx:
            logging.debug('Socket "%s" opened. Yield data from socket.', fifo)
            yield piperx.read()
            logging.debug('Socket is empty', fifo)


def start_task(task):
    if DISPATCHER.is_task(task):
        DISPATCHER.start(task)

        return 'Success'.format(task)
    else:
        return 'Error'.format(task)


def pause_task(task):
    if DISPATCHER.is_task(task):
        DISPATCHER.pause(task)

        return 'Success'.format(task)
    else:
        return 'Error'.format(task)


def stop_task(task):
    if DISPATCHER.is_task(task):
        DISPATCHER.stop(task)

        return 'Success'.format(task)
    else:
        return 'Error'.format(task)


def resume_task(task):
    if DISPATCHER.is_task(task):
        DISPATCHER.resume(task)

        return 'Success'.format(task)
    else:
        return 'Error'.format(task)


def kill_task(task):
    if DISPATCHER.is_task(task):
        DISPATCHER.kill(task)

        return 'Success'.format(task)
    else:
        return 'Error'.format(task)


def kill_all(param=None):
    DISPATCHER.kill_all()

    return 'All task killed'


def _task_is_running(task):
    state = None

    try:
        state = DISPATCHER.get_state(task)
    except Connection.ConnectionAlreadyClosedError:
        pass

    if (state == RUNNING) or (
            state == INITIALIZED and state.transitioning):
        return True

    return False


def stop_wait_and_kill(task):
    if task and _task_is_running(task):
        DISPATCHER.stop(task)

        logging.info("Wait for task {}".format(task))
        try:
            DISPATCHER.join(task, 5)
        except TaskNotStoppedInTimeError:
            logging.info("Task {} didn't stop in time. Kill it.".format(task))

            DISPATCHER.kill(task)

        logging.info("Now end the task")
        DISPATCHER.end(task)


def list_tasks(arg=None):
    logging.debug('Create list of tasks')

    states = []

    for task_ in DISPATCHER.list_tasks():
        logging.debug('Retrieve state of task %s', task_)
        try:
            state = DISPATCHER.get_state(task_)
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
            "{task}\t{state}".format(task=task_, state=state)
        )

    return "\n".join(states)


def system_exit(arg=None):
    global RUN

    logging.info('Shutdown easysched...')

    tasks = DISPATCHER.list_tasks()

    logging.debug('Stop all tasks and wait for them...')
    for task_ in tasks:
        stop_wait_and_kill(task_)

    RUN = False


DISPATCHER = Dispatcher()

COMMAND_MAP = {
    command.CMD_TASK_START: start_task,
    command.CMD_TASK_PAUSE: pause_task,
    command.CMD_TASK_STOP: stop_task,
    command.CMD_TASK_RESUME: resume_task,
    command.CMD_TASK_KILL: kill_task,
    command.CMD_TASK_KILL_ALL: kill_all,
    command.CMD_TASK_LIST: list_tasks,
    command.CMD_SYSTEM_EXIT: system_exit,
}

# Global veriable to let easysched run
RUN = True


def init_commands():
    """ Initialize the command interpreter """
    for cmd in COMMAND_MAP:
        logging.info('Add command "%s"', cmd)
        add_command(cmd, COMMAND_MAP[cmd])


def init():
    # parse arguments
    arguments = parse_arguments()

    # load the configuration
    configuration = Config.load_configuration(arguments.config)

    if CONFIG_SECTION_BASE not in configuration:
        raise InvalidConfigurationError(
            'There is no section "{}" in the configuration'.format(CONFIG_SECTION_BASE))

    elif CONFIG_OPTION_LOG not in configuration[CONFIG_SECTION_BASE]:
        raise InvalidConfigurationError(
            'Option "{}" is missing in section "{}"'.format(
                CONFIG_OPTION_LOG, CONFIG_SECTION_BASE))

    # create the directories defined in the configuration
    Config.create_directories(configuration)

    # initialize the logging module
    initialize(
        arguments.log_level,
        configuration[CONFIG_SECTION_BASE][CONFIG_OPTION_LOG] +
        os.sep +
        MODULENAME + ".log",
        "easysched")

    tasks = create_tasks(configuration['tasks'])

    for task_ in tasks:
        logging.info("Add task %s", task_)
        DISPATCHER.add(task_)


def init_fifos(directory):
    """
    Initialize the fifos for the communication

    Args:
        directory:

    Returns:

    """
    fiforx = os.path.join(directory, FIFO_RX)
    fifotx = os.path.join(directory, FIFO_TX)

    if not os.path.exists(fiforx):
        os.mkfifo(fiforx)

    if not os.path.exists(fifotx):
        os.mkfifo(fifotx)

    return fiforx, fifotx


def main():
    """ Main routine of this module """

    easysched_lock = lock(
        os.path.join(
            TMP_DIR,
            MODULENAME))

    try:

        init()

        init_commands()

        # add easysched to the tmp directory to let the control tool find that directory
        with tempfile.TemporaryDirectory("easysched") as tmp_dir:

            # take care that others can read the temp directory
            os.chmod(tmp_dir, 0o777)

            fiforx, fifotx = init_fifos(tmp_dir)

            # furthermore, other need write rights to write to the rx fifo
            # take care that others can read the temp directory
            os.chmod(fiforx, 0o777)

            while RUN:

                line = ""

                logging.info('Wait for commands')
                # read in the command
                for character in read_fifo(fiforx):

                    line = line + character

                    if os.linesep in line:
                        line = line[:-1]
                        break

                logging.info('received "%s"', line)

                # check if the command is valid
                logging.info('Parse command "%s"', line)
                cmd, parameters = parse_command(line)

                logging.debug('Func: %s, Params: %s', command, parameters)

                if not cmd:
                    logging.warning('Error: statement "%s" is invalid', line)
                    feedback = 'Statement "{}" is invalid'.format(line)
                else:

                    if isinstance(parameters, list) and len(parameters) == 1:
                        feedback = cmd[0](parameters[0])
                    else:
                        parameters = [p.trim() for p in parameters]
                        feedback = cmd[0](parameters)

                # send the feedback if there is any
                if not feedback:
                    feedback = '\n'
                # open the write fifo
                logging.debug('Open fifo %s for sending feedback', fifotx)

                with open(fifotx, mode='w') as pipetx:
                    logging.debug('Send feedback "%s"', feedback)
                    pipetx.write(feedback + "\n")

    finally:
        unlock(easysched_lock)


if __name__ == '__main__':
    main()
