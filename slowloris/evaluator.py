# -*- coding: utf-8 -*-

from copy import deepcopy
from asserts import assert_exp_length, assert_valid_definition, assert_boolean
from ast import is_boolean, is_atom, is_symbol, is_list, is_closure, is_number, is_string
from parser import unparse
from types import Environment, LispError, LispTypeError, Closure

operators = {}


def evaluate(ast, env):
    """Evaluate an Abstract Syntax Tree in the specified environment."""
    if is_symbol(ast):
        if ast[0] == '"':
            return ast
        return env.lookup(ast)
    elif is_atom(ast):
        return ast
    elif is_list(ast):
        return eval_list(ast, env)
    else:
        raise LispError('Syntax error: %s' % unparse(ast))


def eval_list(ast, env):
    """A helper method, to evaluate the common list-form AST"""
    if ast[0] == 'quote':
        return eval_quote(ast, env)
    elif ast[0] == 'exit':
        return eval_exit(ast, env)
    elif ast[0] == 'print':
        return eval_print(ast, env)
    elif ast[0] == 'atom':
        return eval_atom(ast, env)
    elif ast[0] == 'let':
        return eval_let(ast, env)
    elif ast[0] == 'def':
        return eval_def(ast, env)
    elif ast[0] == 'lambda':
        return eval_lambda(ast, env)
    elif ast[0] == 'eq':
        return eval_eq(ast, env)
    elif ast[0] == 'if':
        return eval_if(ast, env)
    elif ast[0] == 'cons':
        return eval_cons(ast, env)
    elif ast[0] == 'head':
        return eval_head(ast, env)
    elif ast[0] == 'tail':
        return eval_tail(ast, env)
    elif ast[0] == 'empty':
        return eval_empty(ast, env)
    elif ast[0] in ['+', '-', '*', '/', 'mod', '<', '<=', '=', '!=', '>=', '>']:
        return eval_math(ast, env)
    elif ast[0] in ['str_append', 'str_split']:
        return eval_string(ast, env)
    elif is_closure(ast[0]):
        return apply(ast, env)
    elif is_symbol(ast[0]) or is_list(ast[0]):
        return evaluate([evaluate(ast[0], env)] + ast[1:], env)
    else:
        raise LispError('%s is not a function' % unparse(ast[0]))


def eval_atom(ast, env):
    assert_exp_length(ast, 2)
    return type(evaluate(ast[1], env)) != list


def apply(ast, env):
    closure = ast[0]
    args = ast[1:]
    if len(args) != len(closure.params):
        msg = "wrong number of arguments, expected %d got %d" \
            % (len(closure.params), len(args))
        raise LispError(msg)
    args = [evaluate(a, env) for a in args]
    bindings = dict(zip(closure.params, args))
    new_env = closure.env.extend(bindings)
    return evaluate(closure.body, new_env)


def eval_cons(ast, env):
    assert_exp_length(ast, 3)
    ls = evaluate(ast[2], env)
    if not is_list(ls):
        raise LispError('The second argument of cons should be a list.')
    return [evaluate(ast[1], env)] + ls


def eval_def(ast, env):
    assert_valid_definition(ast[1:])
    env.set(ast[1], evaluate(ast[2], env))

    return ast[1]


def eval_empty(ast, env):
    assert_exp_length(ast, 2)
    ls = evaluate(ast[1], env)
    if not is_list(ls):
        raise LispError('The argument of empty should be a list.')
    return len(ls) == 0


def eval_env_vars(ast, env):
    if len(env.variables[ast[0]].params) != len(ast) - 1:
        e = "wrong number of arguments, expected %d got %d" % \
            (len(env.variables[ast[0]].params), len(ast) - 1)
        raise LispError("wrong number of arguments, expected 2 got 3")
    vals = [evaluate(t, env) for t in ast[1:]]
    return evaluate([env.variables[ast[0]]] + vals, env)


def eval_eq(ast, env):
    assert_exp_length(ast, 3)
    if type(evaluate(ast[1], env)) == list or type(evaluate(ast[2], env)) == list:
        return False
    else:
        return evaluate(ast[1], env) == evaluate(ast[2], env)


def eval_exit(ast, env):
    assert_exp_length(ast, 1)
    exit()


def eval_head(ast, env):
    assert_exp_length(ast, 2)
    ls = evaluate(ast[1], env)
    if not is_list(ls):
        raise LispError('The argument of head should be a list.')
    elif len(ls) == 0:
        raise LispError('And empty list has no head.')
    return ls[0]


def eval_if(ast, env):
    if evaluate(ast[1], env):
        return evaluate(ast[2], env)
    else:
        return evaluate(ast[3], env)


def eval_lambda(ast, env):
    if len(ast) != 3:
        # TODO: Fix this test. This is silly.
        raise LispError('Wrong number of arguments to lambda form')

    if not is_list(ast[1]):
        raise LispError('The parameters of lambda should be a list.')

    return Closure(env, ast[1], ast[2])


def eval_let(ast, env):
    assert_valid_definition(ast[1:-1])
    env.set(ast[1], evaluate(ast[2], env))

    return evaluate(ast[3], env)


def eval_math(ast, env):
    """helper method to evaluate simple mathematical statements"""
    ops = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
        'mod': lambda a, b: a % b,
        '<': lambda a, b: a < b,
        '<=': lambda a, b: a <= b,
        '=': lambda a, b: a == b,
        '!=': lambda a, b: a != b,
        '>=': lambda a, b: a >= b,
        '>': lambda a, b: a > b
    }
    op = ast[0]
    a = evaluate(ast[1], env)
    b = evaluate(ast[2], env)
    if is_number(a) and is_number(b):
        return ops[op](a, b)
    else:
        raise LispTypeError("Unsupported argument type for %s" % op)


def eval_print(ast, env):
    assert_exp_length(ast, 3)
    print(evaluate(ast[1], env))
    return evaluate(ast[2], env)


def eval_quote(ast, env):
    assert_exp_length(ast, 2)
    return ast[1]


def eval_string(ast, env):
    """helper method to evaluate simple string operations"""
    ops = {
        'str_append': lambda a, b: a[:-1] + b[1:],
        'str_split': lambda a, b: "'" + '("' + '" "'.join(a[1:-1].split(b[1:-1])) + '")'
    }
    op = ast[0]
    if is_string(ast[1]) and is_string(evaluate(ast[2], env)):
        return ops[op](ast[1], evaluate(ast[2], env))
    else:
        print 'last ast ', ast[1], ast[2]
        raise LispTypeError("Unsupported argument type for %s" % op)


def eval_tail(ast, env):
    lst = evaluate(ast[1], env)
    return lst[1:]
