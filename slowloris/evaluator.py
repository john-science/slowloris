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
operators = {}


def evaluate(ast, env):
    """Evaluate an Abstract Syntax Tree in the specified environment.
    
    TODO: What is with this Environment object?
    """
    # TODO: These if-statements are ugly! I need to make this more extensible. (But still fast!?!)
    if type(ast) == list:
        if ast[0] == 'quote':
            if len(ast) > 2:
                raise LispError('quote only takes one argument.')  # TODO: does this cut off the rest of my AST?
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
        else:
            if type(ast[1]) != type(ast[2]):
                if type(ast[1]) not in [int, float] or type(ast[2]) not in [int, float]:
                    raise LispError('Cannot add type %s to type %s.' % (str(type(ast[1])), str(type(ast[2]))))
            if ast[0] == '+':  # TODO: Verify this will work: (+ (+ 1 2) (+ 3 4))
                return ast[1] + ast[2]  # TODO: Am I cutting off the rest of the AST?
            elif ast[0] == '-':
                return ast[1] - ast[2]
            elif ast[0] == '*':
                return ast[1] * ast[2]
            elif ast[0] == '/':
                return ast[1] / ast[2]
            elif ast[0] == 'mod':
                return ast[1] % ast[2]  # TODO: Am I cutting off the rest of the AST?
            elif ast[0] == '<':
                return ast[1] < ast[2]
            elif ast[0] == '=':
                return ast[1] == ast[2]
            elif ast[0] == '>':
                return ast[1] > ast[2]
    
    return ast

