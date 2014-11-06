# -*- coding: utf-8 -*-
import copy

"""
This module holds some types we'll have use for along the way.

It's your job to implement the Closure and Environment types.
The LispError class you can have for free :)
"""


class LispError(Exception):
    """General lisp error class."""
    pass


class LispTypeError(LispError):
    """A LispError subclass, for type errors."""
    pass


class Closure:

    def __init__(self, env, params, body):
        self.env = env
        self.params = params
        self.body = body

    def __str__(self):
        return "<closure/%d>" % len(self.params)


class Environment:

    def __init__(self, variables=None):
        self.variables = variables if variables else {}

    def lookup(self, symbol):
        if symbol not in self.variables:
            raise LispError('%s not in the environment.' % str(symbol))
        return self.variables[symbol]

    def extend(self, variables):
        vs = Environment(copy.deepcopy(self.variables))

        for key,val in variables.iteritems():
            vs.variables[key] = val

        return vs

    def set(self, symbol, value):
        if symbol in self.variables:
            raise LispError('%s already defined' % str(symbol))
        self.variables[symbol] = value

    def set_overwrite(self, symbol, value):
        if symbol not in self.variables:
            raise LispError('%s not defined' % str(symbol))
        self.variables[symbol] = value
