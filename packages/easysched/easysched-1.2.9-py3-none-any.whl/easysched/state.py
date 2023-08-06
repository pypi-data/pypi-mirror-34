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
from copy import copy
from queue import Empty
from time import time


class NoNextStateAvailableError(RuntimeError):
    """ Error if there is no next state """
    pass


class Transition(object):

    def __init__(self, action, condition, nxt, interval=0):
        self.Action = action
        self.Condition = condition
        self.Next = nxt
        self.Interval = interval

    def __str__(self):
        return "[ {}/{} -->{}]".format(self.Condition,
                                       self.Action,
                                       self.Next)

    def __repr__(self):
        try:
            return "[ {}/{} -->{}]".format(str(self.Condition),
                                           str(self.Action),
                                           str(self.Next))
        except TypeError as e:
            print(e)


class State(object):

    def __init__(self, name):

        if "*" in name:
            self._changing = True
            self._name = name.replace("*", "")
        else:
            self._changing = False
            self._name = name

    def __repr__(self, *args, **kwargs):
        return self.name

    def __str__(self):
        if self.transitioning:
            return "{}*".format(self.name)
        else:
            return str(self.name)

    def __eq__(self, obj):
        if isinstance(obj, str):
            return self.name == obj
        elif isinstance(obj, State):
            return self.name == obj.name
        else:
            return self.name == str(obj)

    def __ne__(self, obj):
        return not (self == obj)

    def __hash__(self):
        return hash(self.name)

    @property
    def name(self):
        return self._name

    @property
    def transitioning(self):
        return self._changing

    @transitioning.setter
    def transitioning(self, flag):
        self._changing = flag


# create a NONESTATE
NONESTATE = State(name=str(None))


class Action(object):

    def __init__(self, name, func):
        self.Name = name
        self.Func = func

    def run(self, params=None):

        if self.Func:
            return self.Func(params)

        return True

    def __eq__(self, obj):
        return self.Name == obj.Name and self.Func == obj.Func

    def __repr__(self):
        return self.Name

    def __str__(self):
        return self.Name


class Condition(object):

    def __init__(self, args=None, name=None, blocking=False):
        self.Name = name
        self.Args = args
        self.Blocking = blocking

    def __repr__(self):
        return str(self.Name)

    def __str__(self):
        return str(self.Name)

    def valid(self, queue, blocking=False):

        if self.Args:
            # if argument is given, check if it is true
            if self.Blocking:

                # check if the item in Args is in the queue blocked
                return is_item_in_queue_blocked(self.Args, queue)

            else:
                return is_item_in_queue_nonblocked(self.Args, queue)
        else:
            # if no argument given, condition is always true
            return True


def is_item_in_queue_nonblocked(item, queue_):

    try:
        value = queue_.get_nowait()
    except Empty:
        return False

    if value and item == value:
        logging.debug('Found item {} in queue {}'.format(item, queue_))
        return True
    else:
        queue_.put(value)

    return False


def is_item_in_queue_blocked(item, queue_):

    try:
        value = queue_.get()
    except Empty:
        return False

    if value and item == value:
        logging.debug('Found item {} in queue {}'.format(item, queue_))
        return True
    else:
        queue_.put(value)

    return False


class Statemachine(object):

    def __init__(self, statechart, start_state, queue):

        self.Graph = copy(statechart)
        self.StartState = start_state
        self.State = start_state
        self.Time = 0
        self.Queue = queue
        self.Handlers = []

    def register_notification(self, queue):
        self.Handlers.append(queue)

    def run(self):

        transitions = self.Graph[self.State]

        for transition in transitions:

            # check for a valid condition
            if transition.Condition.valid(self.Queue):

                if transition.Interval < (time() - self.Time):

                    # indicate that we're currently taking the transition between
                    # states
                    self.State.transitioning = True
                    self._notify_new_state()

                    logging.debug('Will take transition %s', transition)

                    self.Time = time()

                    if transition.Action:
                        transition.Action.run()

                    self.State.transitioning = False
                    self._notify_new_state()

                    self.State = transition.Next
                    self._notify_new_state()

                    break

        if self.State is NONESTATE:
            raise NoNextStateAvailableError()

    def get_state(self):
        return self.State

    def reset(self):
        self.State = self.StartState

    def _notify_new_state(self):
        """
        Notifies the registered handlers of a new state
        """

        for handlers in self.Handlers:
            handlers.put(self.State)
