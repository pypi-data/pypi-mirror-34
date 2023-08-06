#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (c) 2016-2018 by Lars Klitzke, Lars@klitzke-web.de
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


""" Tools for reading the configuration file

This modules contains methods and for reading
the configuration file used by this project.
"""

import configparser
import logging
import os
from configparser import ExtendedInterpolation

# Default task tag
TASK_TAG = 'Task:'


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

    config['tasks'] = []

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

                config['tasks'].append(section_def)
            else:
                config[sec] = section_def

    return config


def create_directories(config):
    try:
        for section in config:
            for option in config[section]:
                if '-dir' in option:
                    directory = os.path.abspath(
                        config[section][option])
                    try:
                        logging.info(
                            "Create directory '%s'",
                            directory)
                        os.makedirs(directory)
                    except FileExistsError:
                        pass
    except PermissionError:
        logging.error(
            'Permission denied to create directory in %s.',
            directory)
