#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# This is the interface to the easysched server
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
import sys
import textwrap

import psutil

from easysched.command import register, parse, CMD_TASK_LIST, COMMANDS, CMD_TASK_KILL_ALL, CMD_TASK_KILL, \
    CMD_TASK_RESUME, CMD_TASK_STOP, CMD_TASK_PAUSE, CMD_TASK_START
from easysched.server import EASYSCHED_DEAMON, DEFAULT_PORT
from easysched.state import State
from easysched.task import NONESTATE, IDLE, PAUSED, RUNNING, INITIALIZED
from easysched.tools.logging import initialize

PIPERX = None
PIPETX = None

FILENAME_TX = None
FILENAME_RX = None

# Name of this tool
EASYSCHED_CONTROL = "esdctrl"




class EasyschedNotRunningError(Exception):
    pass


class TaskUnknownError(Exception):
    pass


class EasyschedController(object):
    """
    Interface to the easysched daemon.
    """

    def _write(self, message):
        """ Sends the message to the easysched deamon """

        async def write_read(message, loop):

            reader, writer = await asyncio.open_connection(
                host=self._host,
                port=self._port,
                loop=loop)

            writer.write(message.encode())

            feedback = await reader.read()

            writer.close()

            return json.loads(feedback.decode())

        if not message.endswith("\n"):
            message += "\n"

        result = self._loop.run_until_complete(
            asyncio.wait(
                [write_read(message, self._loop)]
            )
        )

        return result[0].pop().result()

    def _kill(self):
        """Kill the easysched deamon"""
        logging.info("Kill easysched deamon")

        self.esdd.kill()

    def _update_states(self):
        """ Updates the states of the tasks"""

        # send command to list the task states
        result = self._write(CMD_TASK_LIST)

        # parse the result to determine the state of each task
        taskstates = {}

        if result['code'] == 0:
            if 'value' in result:
                for line in result['value'].split("\n"):

                    stripped_line = line.strip()

                    if stripped_line:
                        # there may be an empty line
                        entries = stripped_line.split('\t')
                        taskstates[entries[0]] = State(entries[1])

                logging.info("States of applications {}".format(taskstates))
                self._taskstate = taskstates
            return True
        elif result['code'] == 1:
            return False
        else:
            # in any other case, raise a not implemented error
            raise NotImplementedError("The return value {} is not supported.".format(result))


    def state(self, task):
        """
        Get the state of the `task`

        Args:
            task: Task which state to query

        Returns:
            The `State` of the given `task`

        """

        # update the internal task states
        self._update_states()

        try:
            return self._taskstate[task]
        except KeyError:
            raise TaskUnknownError('The given Task {} is unknown'.format(task))

    def _not_running(self, task):
        """
        Checks if the given `task` is not running

        Args:
            task: Task to check for

        Returns:
            True: Iff the task is not in any of the states `NONESTATE`, `IDLE` or `PAUSED`
            False: otherwise

        """
        state = self.state(task)

        return (state == NONESTATE
                or state == IDLE
                or state == PAUSED)

    def _running(self, task):
        """
        Checks if the given `task` is running
        Args:
            task:   Task to check for

        Returns:
            True: If the task is either `RUNNING` or `INITIALIZED` and transitioning

        """
        state = self.state(task)

        return (state == RUNNING) or (
                state == INITIALIZED and state.transitioning
        )

    def start(self, task):
        """
        Start the given `task`

        Args:
            task: Task to start

        Returns:
            True: On success
            False: Otherwise

        """
        logging.info("Start task {}".format(task))

        state = self.state(task)

        if state == NONESTATE or state == IDLE:
            return self.write_cmd(CMD_TASK_START, task)
        elif state == PAUSED:
            return self.write_cmd(CMD_TASK_RESUME, task)
        else:
            logging.warning("Task %s is already running", task)

    def pause(self, task):
        """
        Pauses the given `task`

        Args:
            task: Task to pause

        Returns:
            True: On success
            False: Otherwise
        """

        if self._running(task):
            return self.write_cmd(CMD_TASK_PAUSE, task)
        else:
            logging.warning("Task %s is not running", task)

    def stop(self, task):
        """
        Stops the given `task`

        Args:
            task: Task to pause

        Returns:
            True: On success
            False: Otherwise
        """
        if self._running(task):
            return self.write_cmd(CMD_TASK_STOP, task)
        else:
            logging.warning("Task %s is not running", task)

    def terminate(self, task):
        """
        Terminates the given `task`

        Args:
            task: Task to pause

        Returns:
            True: On success
            False: Otherwise
        """
        return self.write_cmd(CMD_TASK_KILL, task)

    def terminate_all(self):
        """
        Terminates all tasks

        Returns:
            True: On success
            False: Otherwise
        """
        return self._write(CMD_TASK_KILL_ALL)

    def write_cmd(self, cmd, *args):
        """
        Sends the given `cmd` to the easysched daemon

        Args:
            cmd:    Command to send, see `command` module
            args:   List of argumnets

        """
        if not isinstance(args, tuple) and not isinstance(args, list):
            args = [*args]

        result = self._write(cmd.replace("*", "{}").format(*args))

        if result['code'] == 0:
            if 'value' in result:
                return result['value']
            return True
        elif result['code'] == 1:
            return False
        else:
            # in any other case, raise a not implemented error
            raise NotImplementedError("The return value {} is not supported.".format(result))

    @property
    def name(self):
        return self._name

    @property
    def esdd(self):
        """
        The easysched deamon process

        Returns:
            The easysched deamon process as `psutil.Process`

        """

        for proc in psutil.process_iter():
            if proc.name() == EASYSCHED_DEAMON:
                return proc

        raise EasyschedNotRunningError('Cannot find the easysched process')

    def __init__(self, loop=None, host='127.0.0.1', port=DEFAULT_PORT):

        if loop is None:
            loop = asyncio.get_event_loop()

        self._loop = loop
        self._name = EASYSCHED_CONTROL

        self._host = host
        self._port = port


def parse_arguments():
    """ Parses the program arguments"""

    arg_parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                         description="""
                                        esctrl is the interface to the easysched server.""",
                                         epilog=textwrap.dedent("""'
Use this tool to interact with the server of easysched. 
                              
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

    arg_parser.add_argument('--port', help="The easysched is listening to", default=DEFAULT_PORT)
    arg_parser.add_argument('cmd', help="The command to send to the server", nargs="*")

    return arg_parser.parse_args()


def main():

    args = parse_arguments()

    initialize(level=logging.WARNING)

    esdctrl = EasyschedController(port=args.port)

    # for each command in Comman add our handler
    for command in COMMANDS:
        register(command, esdctrl.write_cmd, command)

    if len(sys.argv) == 1:
        logging.error('Error: You have to pass a statement')
        sys.exit(-1)

    func, params = parse(" ".join(args.cmd))

    if not func:
        logging.error('Error: statement "%s" is invalid', " ".join(args.cmd))
        sys.exit(-1)

    try:
        print(func.execute(*params))
    except ConnectionRefusedError:
        logging.error('Cannot connect to easysched - is it running?')

    logging.debug('Cleanup and exit')


if __name__ == '__main__':

    main()
