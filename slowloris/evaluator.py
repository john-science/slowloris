# -*- coding: utf-8 -*-

from types import Environment, LispError, Closure
from ast import is_boolean, is_atom, is_symbol, is_list, is_closure, is_integer, is_number
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
    """Evaluate an Abstract Syntax Tree in the specified environment."""
    # TODO: These if-statements are ugly! I need to make this more extensible. (But still fast!?!)
    # TODO: Am I cutting off the rest of the AST with the below statements?
    if is_atom(ast):
        return ast
    elif is_symbol(ast):
        return env.lookup(ast)
    elif is_list(ast):
        return eval_list(ast, env)
    else:
        raise LispError('Syntax error: %s' % unparse(ast))

def eval_list(ast, env):
    """A helper method, to evaluate the common list-form AST"""
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
    elif ast[0] == 'cons':
        assert_exp_length(ast, 3)
        ls = evaluate(ast[2], env)
        if not is_list(ls):
            raise LispError('The second argument of cons should be a list.')
        return [evaluate(ast[1], env)] + ls
    elif ast[0] == 'head':
        assert_exp_length(ast, 2)
        ls = evaluate(ast[1], env)
        if not is_list(ls):
            raise LispError('The argument of head should be a list.')
        elif len(ls) == 0:
            raise LispError('And empty list has no head.')
        return ls[0]
    elif ast[0] == 'tail':
        assert_exp_length(ast, 2)
        ls = evaluate(ast[1], env)
        if not is_list(ls):
            raise LispError('The argument of tail should be a list.')
        elif len(ls) == 0:
            raise LispError('And empty list has no tail.')
        return ls[1:]
    elif ast[0] == 'empty':
        assert_exp_length(ast, 2)
        ls = evaluate(ast[1], env)
        if not is_list(ls):
            raise LispError('The argument of empty should be a list.')
        return len(ls) == 0
    elif ast[0] in ['+', '-', '*', '/', 'mod', '<', '=', '!=', '>']:
        return eval_math(ast, env)
    elif is_closure(ast[0]):
        if len(ast) == 1:
            return evaluate(ast[0].body, ast[0].env)
        else:
            vals = [evaluate(t, env) for t in ast[1:]]
            return evaluate(ast[0].body, ast[0].env.extend(dict(zip(ast[0].params, vals))))
    elif ast[0] in env.variables.keys():
        if len(env.variables[ast[0]].params) != len(ast) - 1:
            e = "wrong number of arguments, expected %d got %d" % \
                (len(env.variables[ast[0]].params), len(ast) - 1)
            raise LispError("wrong number of arguments, expected 2 got 3")
        vals = [evaluate(t, env) for t in ast[1:]]
        return evaluate([env.variables[ast[0]]] + vals, env)
    elif is_list(ast[0]):
        return evaluate([evaluate(ast[0], env)] + ast[1:], env)
    else:
        raise LispError('%s is not a function' %s unparse(ast[0]))


def eval_math(ast, env):
    """helper method to evaluate simple mathematicl statements"""
    # TODO: Should these statements should work for more than two values? How about just +?
    #       IF not, should I put a check on the length of the arguments?
    ops = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
        'mod': lambda a, b: a % b,
        '<': lambda a, b: a < b,
        '=': lambda a, b: a == b,
        '!=': lambda a, b: a != b,
        '>': lambda a, b: a > b
    }
    op = ast[0]
    a = evaluate(ast[1], env)
    b = evaluate(ast[2], env)
    if is_number(a) and is_number(b):
        return ops[op](a, b)
    else:
        raise LispError("Unsupported argument type for %s" % op)
