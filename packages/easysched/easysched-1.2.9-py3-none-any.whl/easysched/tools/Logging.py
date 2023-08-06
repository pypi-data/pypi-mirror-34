# -*- coding: utf-8 -*-

# Copyright (c) 2016-2018 by Lars Klitzke, lars@klitzke-web.de.
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


""" Tools for extended logging functionality

This modules initializes the root logger instance and
enables logging to a file and to stdout simultaneously
by just using the default log function of the logging
class.

"""

import logging
import sys


class LevelDependFormat(logging.Formatter):
    ''' A custom format for logging with level-dependend text colors'''

    # see https://en.wikipedia.org/wiki/ANSI_escape_code
    COLOR_CODES = {
        logging.INFO: "\033[1m",
        logging.WARNING: "\033[1;33;40m",
        logging.DEBUG: "\33[1;30;40m",
        logging.ERROR: '\033[1;91m',
        logging.CRITICAL: '\033[6;31;40m',

    }

    ENDC = '\033[0m'

    MSG_TEMPLATE = "{start}[%(asctime)s | %(module)s:%(funcName)s:%(lineno)d] <%(processName)s::%(threadName)s> %(levelname)s:  %(message)s{end}"

    def __init__(self, fmt=None):
        fmt = self.MSG_TEMPLATE.format(
            start=self.COLOR_CODES[logging.INFO],
            end=self.ENDC)
        logging.Formatter.__init__(self, fmt)

    def format(self, record):
        '''Custom format function to select the format map w.r.t log-level.'''

        # save the format
        format_orig = self._fmt

        # retrieve the template by the error level
        if record.levelno in self.COLOR_CODES:
            self._fmt = self.MSG_TEMPLATE.format(
                start=self.COLOR_CODES[
                    record.levelno],
                end=self.ENDC)

        # now format the output
        result = logging.Formatter.format(self, record)

        # restore the format
        self._fmt = format_orig

        return result


def initialize(level, filename=None, prefix=None):
    ''' Initialize the logger

    Keyword arguments:
    level --- Logging level, see logging class for available levels
    filname --- Optional argument defining the log file

    '''
    root_logger = logging.getLogger()

    # remove the default handler
    if root_logger.handlers:
        root_logger.removeHandler(root_logger.handlers[0])

    # create a format for the logging as well for file logging as for
    # logging to stdout
    if prefix:
        log_format = logging.Formatter(
            "[%(asctime)s | %(module)s:%(lineno)d] <%(processName)s:%(threadName)s> [[{}]] %(levelname)s:  %(message)s".format(prefix))
    else:
        log_format = logging.Formatter(
            "[%(asctime)s | %(module)s:%(lineno)d] <%(processName)s::%(threadName)s> %(levelname)s:  %(message)s")

    # retrieve the root logger - we only use one
    root_logger.setLevel(level)

    # setup the file logging
    if filename:
        file_handler = logging.FileHandler(filename)
        file_handler.setFormatter(log_format)
        root_logger.addHandler(file_handler)

    # setup the console logging - log to stdout
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(LevelDependFormat())
    root_logger.addHandler(console_handler)
