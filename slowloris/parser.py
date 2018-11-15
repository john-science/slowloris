# -*- coding: utf-8 -*-

import re
from ast import is_boolean, is_list, is_decimal
from types import LispError

"""
This is the parser module, with the `parse` function which you'll implement as part 1 of
the workshop. Its job is to convert strings into data structures that the evaluator can
understand.
"""
# a dict that associates each method with its decorator
decorators = dict()


def parse(source):
    """Parse string representation of one *single* expression
    into the corresponding Abstract Syntax Tree."""

    # remove comments from the source code
    source = remove_comments(source)

    # create the AST from the Slow Loris text
    ast = parse_text(source)
    # detect decorators
    ast = parse_deco(ast)
    # parse the AST into the various possible types
    ast = parse_types_deep(ast)
    # change the AST if there is a decorator associated with the method
    ast = generate_new_ast(ast)

    return ast


def generate_new_ast(ast):
    """
    a method to generate a new AST if there is a decorator associated with current method
    """
    try:
        if ast:
            if ast[0] in decorators:
                associated_decorator = decorators[ast[0]]
                new_ast = [associated_decorator]
                new_ast.append(ast)
                return new_ast
    except TypeError:
        return ast

    return ast


def parse_deco(ast):
    """ method that detects decorator and associate each method with its specified decorator """
    if ast:
        if '@' == ast[0][0] and len(ast[0]) >= 4:
            decorator = ast[0][1:]
            to_be_decorated = ast[1][1]
            decorators[to_be_decorated] = decorator
            return ast[1]

    return ast


def parse_text(source):
    """Recursive method to parse the Slow Loris text into an AST"""
    # if type is list
    if type(source) == list:
        for i in range(len(source)):
            source[i] = parse_text(source[i])
        return source

    # type is string
    if len(source) > 0 and source[0] == "'":
        return ['quote', parse_text(source[1:])]
    elif '(' in source:
        start = source.find('(')
        end = find_matching_paren(source, start)
        if end == -1:
            raise LispError("Incomplete expression: %s" % source[start:])
        last = parse_text(source[end+1:])
        if last:
            return parse_text(split_exps(source[start+1: end])) + [last]
        else:
            return parse_text(split_exps(source[start+1: end]))
    elif ')' in source:
        raise LispError("Expected EOF")
    else:
        return source.strip()


def parse_type(src):
    """convert a string to an implicit type, if it exists"""
    if src.isdigit():
        return int(src)
    elif is_decimal(src):
        return float(src)
    elif src == 'False':
        return False
    elif src == 'True':
        return True

    return src


def parse_types_deep(ast):
    if type(ast) == list:
        for i in range(len(ast)):
            ast[i] = parse_types_deep(ast[i])
        return ast
    else:  # type is str
        return parse_type(ast)


##
## Below are a few useful utility functions.
##


def remove_comments(source):
    """Remove from a string anything in between a # and a linebreak"""

    return re.sub(r"#.*\n", "\n", source)


def find_matching_paren(source, start=0):
    """Given a string and the index of an opening parenthesis, determines
    the index of the matching closing paren."""

    assert source[start] == '('
    pos = start
    open_brackets = 1
    while open_brackets > 0:
        pos += 1
        if len(source) == pos:
            raise LispError("Incomplete expression: %s" % source[start:])
        if source[pos] == '(':
            open_brackets += 1
        if source[pos] == ')':
            open_brackets -= 1
    return pos


def split_exps(source):
    """Splits a source string into subexpressions
    that can be parsed individually.

    Example:

        > split_exps("foo bar (baz 123)")
        ["foo", "bar", "(baz 123)"]
    """

    rest = source.strip()
    exps = []
    while rest:
        exp, rest = first_expression(rest)
        exps.append(exp)

    # if '@' in exps[1:]:
    #     raise LispError('no nested decorator ')
    #
    # if '@' in exps[0]:
    #     exps[0] = exps[0][1:]

    return exps


def first_expression(source):
    """Split string into (exp, rest) where exp is the
    first expression in the string and rest is the
    rest of the string after this expression.
    """
    source = source.strip()
    if source[0] == "'":
        exp, rest = first_expression(source[1:])
        return source[0] + exp, rest
    elif source[0] == "(":
        last = find_matching_paren(source)
        return source[:last + 1], source[last + 1:]
    else:
        # This regex also uses quotes to Identify strings.
        match = re.match(r'(?:"[^"]*"|[^\s"])+', source)
        end = match.end()
        atom = source[:end]
        return atom, source[end:]


##
## The functions below, `parse_multiple` and `unparse` are implemented in order for
## the REPL to work.
##


def parse_multiple(source):
    """Creates a list of ASTs from program source constituting multiple expressions.

    Example:

        >>> parse_multiple("(foo bar) (baz 1 2 3)")
        [['foo', 'bar'], ['baz', 1, 2, 3]]

    """

    source = remove_comments(source)
    return [parse(exp) for exp in split_exps(source)]


def unparse(ast):
    """Turns an AST back into lisp program source"""

    if is_boolean(ast):
        return 'True' if ast else 'False'
    elif is_list(ast):
        if len(ast) > 0 and ast[0] == "quote":
            return "'%s" % unparse(ast[1])
        else:
            return "(%s)" % " ".join([unparse(x) for x in ast])
    else:
        # integers or symbols (or lambdas)
        return str(ast)
