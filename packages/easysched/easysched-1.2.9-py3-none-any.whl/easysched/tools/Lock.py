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

""" Tools for securing the execution of a script

This modules contains methods and for managing lock files.
Use this module if you have a task which should only run
once and you want to guarantee this.

Copyright 2016-2017 by Lars Klitzke, lars@klitzke-web.de.
All Rights Reserved.

You can create a lock file by
>>> handle = lock('/tmp/test')
>>> print(handle)
/tmp/test.pid

and check if a lock already exists by is_locked() which
should return True if the second last lock was successful
>>> is_locked(handle)
True

If you now want to lock it another time, an exception is raised
>>> lock('/tmp/test')
Traceback (most recent call last):
FileLockedError: Lock already exists

Finally, you need to release that lock if execution has finished with the handle
>>> unlock(handle)
True
"""

import logging
import os

LOCK_EXTENSION = '.pid'


class FileLockedError(RuntimeError):
    """ Exception if there already is a lock """
    pass


def lock(filename):
    """ create a lock using filename as the name including path to the file

    Keyword arguments:
    filename --- name with path to the lock file but without extension

    Return:
    handle to the lock file on success

    Raises:
    A FileLockedError if file is already locked
    A IOError if lock creation failed or writing to lock failed

    Tests:

    Try to lock a file in /tmp which should be writeable
    >>> handle = lock('/tmp/lock_test')
    >>> print(handle)
    /tmp/lock_test.pid

    """

    lock_file = None

    full_lock_name = filename + LOCK_EXTENSION

    if is_locked(filename):
        # file already exists
        raise FileLockedError('Lock already exists')
    try:
        lock_file = open(full_lock_name, 'w')
    except:
        raise IOError('Failed creating log file {}'.format(full_lock_name))

    try:
        lock_file.close()
    except:
        raise IOError('Failed writing to lock file{}'.format(full_lock_name))

    return full_lock_name


def is_locked(handle):
    """ Checks if the lock already exists

    Keyword arguments:
    handle --- lock either returned from previous call of lock() or the name passed to lock()

    Return:
    True if locked
    False otherwise

    Tests:
    Open a file with the lock extension name
    >>> handle = open('/tmp/is_locked.pid', 'w')
    >>> print(handle.name)
    /tmp/is_locked.pid

    If the previous call was successful, close the handle
    >>> handle.close()

    And check if the file is locked. We can either use
    the full name
    >>> is_locked('/tmp/is_locked.pid')
    True

    or just the name without the extension.
    >>> is_locked('/tmp/is_locked')
    True

    After removing the file
    >>> os.remove('/tmp/is_locked.pid')

    the check if the files is still locked should
    return False for the fullname
    >>> is_locked('/tmp/is_locked.pid')
    False

    and for the name without extension
    >>> is_locked('/tmp/is_locked')
    False
     """

    lock_name = handle

    if lock_name.find(LOCK_EXTENSION) < 0:
        lock_name = lock_name + LOCK_EXTENSION

    if os.path.exists(lock_name):
        logging.debug('We have a lock on that file')
    else:
        logging.debug('No lock available')
        return False

    return True


def unlock(handle):
    """ Removes the lock safely

    Keyword arguments:
    handle --- lock either returned from previous call of lock() or the name passed to lock()


    Return:
    True if lock was removed
    False otherwise

    Raises:
    RuntimeError if argument format is invalid

    Tests:

    Arguments should have the correct format.
    Integers for instance are not allowed
    >>> unlock(12331)
    Traceback (most recent call last):
    RuntimeError: Wrong format of argument

    neither are some other random files
    >>> unlock('/file/not/available')
    Traceback (most recent call last):
    RuntimeError: Argument should specify a lock file

    But, correctly defined files are valid
    >>> handle = open('/tmp/doctest.pid', 'w')
    >>> handle.close()
    >>> unlock('/tmp/doctest.pid')
    True

    """

    if not isinstance(handle, str):
        raise RuntimeError('Wrong format of argument')

    if handle.find(LOCK_EXTENSION) < 0:
        raise RuntimeError('Argument should specify a lock file')

    if is_locked(handle):

        os.remove(handle)

        return True

    return False


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
