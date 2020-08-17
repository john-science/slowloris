# -*- coding: utf-8 -*-

from sl_types import Closure

"""
This module contains a few simple helper functions for 
checking the type of ASTs.
"""


def is_atom(x):
    return is_symbol(x) \
        or is_integer(x) \
        or is_float(x) \
        or is_boolean(x) \
        or is_string(x) \
        or is_closure(x)


def is_boolean(x):
    return isinstance(x, bool)


def is_closure(x):
    return isinstance(x, Closure)


def is_decimal(x):
    try:
        float(x)
        return True
    except:
        return False
    return False


def is_integer(x):
    return isinstance(x, int)


def is_float(x):
    return isinstance(x, float)


def is_list(x):
    return isinstance(x, list)


def is_number(x):
    return is_integer(x) or is_float(x)


def is_string(x):
    if isinstance(x, str):
        return x[0] == '"' and x[-1] == '"'
    return False


def is_symbol(x):
    return isinstance(x, str)
