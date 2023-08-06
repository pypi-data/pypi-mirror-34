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

import configparser
import logging
import os
from configparser import ExtendedInterpolation

# Default task tag
TASK_TAG = 'Task:'

# Dictionary key of the tasks in the configuration dictionary
TASKS_KEY = "tasks"


def load_configuration(file, task_opt='task-tag'):
    """
    Loads in the config defined by file and generates a dictionary of dictionaries for each section

    Arguments:
    file -- Configuration file to parse

    This function will try to parse the configuration file defined by file. Then it will create
    a dictionary with the default entries specified in the DEFAULT section. Additionally, the
    resulting dictionary will contain a list of dictionaries, where a dictionary equals a section
    in the configuration file
    """

    # initialize the configuration parser
    parser = configparser.ConfigParser(interpolation=ExtendedInterpolation())

    if not os.path.exists(file) and os.stat(file).st_size > 0:
        logging.error('Cannot find configuration file %s', file)
        raise RuntimeError(
            "Cannot find configuration file {}".format(file))

    try:
        parser.read(file)

    except configparser.Error as err:

        logging.error(
            "Cannot parse configuration file %s due to error: %s",
            file,
            err,
            exc_info=1)

        raise RuntimeError("Cannot parse configuration file  %s due to error:  %s",
                           file,
                           err)

    defaults = parser.defaults()

    config = {}
    for i in defaults:
        config[i] = parser.get('DEFAULT', i)

    task_tag = TASK_TAG

    config[TASKS_KEY] = []

    logging.info(
        'Found %s sections in the configuration', len(parser.sections()))
    for sec in parser.sections():

        # skip the default section - already handles it
        if sec != 'DEFAULT':

            # init section definition objects
            section_def = {}

            # get the options for each entry
            for opt in parser.options(sec):

                # update the task definition tag if set
                if opt == task_opt:
                    task_tag = parser.get(sec, opt)

                section_def[opt] = parser.get(sec, opt)

            # check if this is a task definition
            if sec.find(task_tag) >= 0:
                # add it to the list
                # remove the tag from the name
                section_def['name'] = sec.replace(task_tag, '')

                config[TASKS_KEY].append(section_def)
            else:
                config[sec] = section_def

    return config


def create_directories(config):
    """
    Create a directory for each option in `config` ending with `-dir`.

    Args:
        config: Configuration dictionary, see `load_configuration`

    """
    for section in config:
        for option in config[section]:
            if isinstance(option, str) and option.endswith('-dir'):

                # support list of directories
                for directory in config[section][option].split(','):
                    logging.info("Create directory '%s'", os.path.abspath(directory))
                    os.makedirs(os.path.abspath(directory), exist_ok=True)
