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

import logging

# Each command should start with CMD_
CMD_TASK_START = "task * start"
CMD_TASK_PAUSE = "task * pause"
CMD_TASK_STOP = "task * stop"
CMD_TASK_RESUME = "task * resume"
CMD_TASK_KILL = "task * kill"
CMD_TASK_KILL_ALL = "task kill all"
CMD_TASK_LIST = "task list"
CMD_SYSTEM_EXIT = "system exit"

# Centrelized list of available commands used by easysched
COMMANDS = [globals()[cmd] for cmd in globals() if "CMD_" in cmd]

# Registered Commands
_REGISTERED_COMMANDS = {}


class InvalidCommandFormatError(RuntimeError):
    """ Error for an invalid command format """
    pass


class Command(object):
    """
    Wrapper class for a callable object with a parameter.

    """
    def __init__(self, func, data):
        """
        Initialize a `Command` with a function and optional `data` passed to `func`
        Args:
            func (callable): The callable to call
            data:            Optional data passed to `func` on call
        """
        super().__init__()

        assert callable(func)

        self._func = func
        self._data = data

    @property
    def func(self):
        return self._func

    @property
    def data(self):
        return self._data

    def execute(self, *args, **kwargs):
        """
        Executes the defined function.

        Notes:
            \*args and \*\*kwargs will be passed as additional parameter to the function

        Returns:
            The result of the function

        """
        if self._data is None:
            return self._func(*args, **kwargs)
        return self._func(self._data, *args, **kwargs)


def register(command, func, data=None):
    """ Registers the `command`

    Args:
        command (str):   The command to register
        func (callable): Callable to call if the `command` occurs
        data:            Optional data passed to `func`


    Command is a str representing a command which should be
    registered. The command is a list of strings.

    You can use the * sign to define a parameter which will
    be passed to the function as parameter.

    The function defined by func will be called upon command
    matching.
    """

    assert isinstance(command, str), 'The command has to be a string'
    assert callable(func), 'The given func parameter is not a callable'

    # wrap parameter into a command
    func = Command(func, data)

    level = _REGISTERED_COMMANDS

    keywords = command.strip().split(' ')

    for i in range(len(keywords)):

        entry = keywords[i]

        if not isinstance(entry, str):
            raise InvalidCommandFormatError(
                'All elements in command has to be of type str')

        # if the entry is not already available, add a dummy dictionary
        if not entry in level and i < len(keywords) - 1:
            level[entry] = dict()

            level = level[entry]

        elif entry in level:
            level = level[entry]

        else:
            logging.debug(
                "Add (%s, %s) to level %s and entry %s",
                func,
                data,
                level,
                entry)
            level[entry] = func


def parse(command):
    """ Parses the given command

    Args:

        command (str): Command to parse

    Returns:

        Command: The registered `Command`
        list:    A list of parameters

    """
    assert isinstance(command, str), 'The command has to be a string'

    search_instance = _REGISTERED_COMMANDS

    cmd = None
    parameters = []

    for entry in command.split(' '):

        # if  entry is a parameter add it to the list
        if entry not in search_instance and '*' in search_instance:
            parameters.append(entry)
            search_instance = search_instance['*']
        # get the next layer if the entry is found
        elif entry in search_instance:
            search_instance = search_instance[entry]
        else:
            # entry not in map, so this is an invalid command
            search_instance = None
            break

    if search_instance:
        cmd = search_instance

    return cmd, parameters
