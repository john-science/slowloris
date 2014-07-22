# -*- coding: utf-8 -*-

from types import Environment, LispError, Closure
from ast import is_boolean, is_atom, is_symbol, is_list, is_closure, is_integer
from asserts import assert_exp_length, assert_valid_definition, assert_boolean
from parser import unparse

"""
This is the Evaluator module. The `evaluate` function below is the heart
of your language, and the focus for most of parts 2 through 6.

A score of useful functions is provided for you, as per the above imports, 
making your work a bit easier. (We're supposed to get through this thing 
in a day, after all.)
"""


def evaluate(ast, env):
    """Evaluate an Abstract Syntax Tree in the specified environment.
    
    TODO: What is with this Environment object?
    """
    # TODO: These if-statements are ugly! I need to make this more extensible. (But still fast!?!)
    if type(ast) == list:
        if ast[0] == 'quote':
            if len(ast) > 2:
                raise LispError('quote only takes one argument.')
            return ast[1]
        elif ast[0] == 'atom':
            if len(ast) > 2:
                raise LispError('atom only takes one argument.')
            return type(evaluate(ast[1], env)) != list  # TODO: Should this be a new Environment()?
        elif ast[0] == 'eq':
            if len(ast) > 3:
                raise LispError('eq only takes two arguments.')
            if type(evaluate(ast[1], env)) == list or type(evaluate(ast[2], env)) == list:
                return False
            else:
                return evaluate(ast[1], env) == evaluate(ast[2], env)  # TODO: Should this be a new Env()?
        elif ast[0] == '+':
            pass
        elif ast[0] == '-':
            pass
        elif ast[0] == '*':
            pass
        elif ast[0] == '/':
            pass
        elif ast[0] == 'mod':
            pass
        elif ast[0] == '<':
            pass
        elif ast[0] == '=':
            pass
        elif ast[0] == '>':
            pass
            
    
    return ast

