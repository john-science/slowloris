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
    """
    # TODO: These if-statements are ugly! I need to make this more extensible. (But still fast!?!)
    # TODO: Am I cutting off the rest of the AST with the below statements?
    if not is_list(ast):
        if is_integer(ast) or is_boolean(ast):
            return ast
        else:
            return env.lookup(ast)

    if ast[0] == 'quote':
        assert_exp_length(ast, 2)
        return ast[1]
    elif ast[0] == 'atom':
        assert_exp_length(ast, 2)
        return type(evaluate(ast[1], env)) != list  # TODO: Should this be a new Environment()?
    elif ast[0] == 'define':
        if len(ast) != 3:
            raise LispError('Wrong number of arguments')  # TODO: the test is stupid
        elif not is_symbol(ast[1]):
            raise LispError('non-symbol')
        
        if is_symbol(ast[2]) or is_list(ast[2]):
            env.set(ast[1], evaluate(ast[2], env))
        else:
            env.set(ast[1], ast[2])
            
        return 'Defined.'
    elif ast[0] == 'lambda':
        # assert_exp_length(ast, 3)  # TODO: the test is stupid
        if len(ast) != 3:
            raise LispError('number of arguments')
        elif not is_list(ast[1]):
            raise LispError('The parameters of lambda should be a list.')
        return Closure(env, ast[1], ast[2])
    elif ast[0] == 'eq':
        assert_exp_length(ast, 3)
        if type(evaluate(ast[1], env)) == list or type(evaluate(ast[2], env)) == list:
            return False
        else:
            return evaluate(ast[1], env) == evaluate(ast[2], env)  # TODO: Should this be a new Env()?
    elif ast[0] == 'if':
        if evaluate(ast[1], env):
            return evaluate(ast[2], env)
        else:
            return evaluate(ast[3], env)
    elif ast[0] in ['+', '-', '*', '/', 'mod', '<', '=', '!=', '>']:
        # TODO: I am relying on Python to catch the type errors in these math interactions.
        #if type(ast[1]) != type(ast[2]):
        #    if type(ast[1]) not in [int, float] or type(ast[2]) not in [int, float]:
        #        raise LispError('Cannot add type %s to type %s.' % (str(type(ast[1])), str(type(ast[2]))))

        if ast[0] == '+':
            return evaluate(ast[1], env) + evaluate(ast[2], env)
        elif ast[0] == '-':
            return evaluate(ast[1], env) - evaluate(ast[2], env)
        elif ast[0] == '*':
            return evaluate(ast[1], env) * evaluate(ast[2], env)
        elif ast[0] == '/':
            return evaluate(ast[1], env) / evaluate(ast[2], env)
        elif ast[0] == 'mod':
            return evaluate(ast[1], env) % evaluate(ast[2], env)
        elif ast[0] == '<':
            return evaluate(ast[1], env) < evaluate(ast[2], env)
        elif ast[0] == '=':
            return evaluate(ast[1], env) == evaluate(ast[2], env)
        elif ast[0] == '!=':
            return evaluate(ast[1], env) != evaluate(ast[2], env)
        elif ast[0] == '>':
            return evaluate(ast[1], env) > evaluate(ast[2], env)
    elif is_closure(ast[0]):
        if len(ast) == 1:
            return evaluate(ast[0].body, ast[0].env)
        else:
            vals = [evaluate(t, env) for t in ast[1:]]
            return evaluate(ast[0].body, ast[0].env.extend(dict(zip(ast[0].params, vals))))
    elif ast[0] in env.variables.keys():
        vals = [evaluate(t, env) for t in ast[1:]]
        return evaluate([env.variables[ast[0]]] + vals, env)

    return ast


# TODO: Remove
def is_float(s):
    """Can the input string be parsed into a float?"""
    try:
        float(s)
        return True
    except:
        return False


# TODO: Remove
def is_int(s):
    """Can the input string be parsed into a int?"""
    try:
        int(s)
        return True
    except:
        return False
