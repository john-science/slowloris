# -*- coding: utf-8 -*-

from nose.tools import assert_equals
from os.path import dirname, relpath, join

from slowloris.interpreter import interpret, interpret_file
from slowloris.types import Environment

env = Environment()
path = join(dirname(relpath(__file__)), '..', 'stdlib.sl')
interpret_file(path, env)

"""
Consider these tests as suggestions for what a standard library for
your language could contain. Each test function tests the implementation
of one stdlib function.

Put the implementation in the file `stdlib.sl` at the root directory
of the repository. The first function, `not` is already defined for you.
It's your job to create the rest, or perhaps somthing completely different?

Anything you put in `stdlib.sl` is also available from the REPL, so feel
free to test things out there.

    $ ./repl
    →  (not #t)
    #f

PS: Note that in these tests, `interpret` is used. In addition to parsing
and evaluating, it "unparses" the result, hence strings such as "#t" as the
expected result instead of `True`.
"""

def test_not():
    """logical operator 'not' should return opposite of given boolean value"""
    assert_equals("#t", interpret('(not #f)', env))
    assert_equals("#f", interpret('(not #t)', env))

def test_or():
    """test the logical 'or' operator"""
    assert_equals("#f", interpret('(or #f #f)', env))
    assert_equals("#t", interpret('(or #t #f)', env))
    assert_equals("#t", interpret('(or #f #t)', env))
    assert_equals("#t", interpret('(or #t #t)', env))

def test_and():
    """test the logical 'and' operator"""
    assert_equals("#f", interpret('(and #f #f)', env))
    assert_equals("#f", interpret('(and #t #f)', env))
    assert_equals("#f", interpret('(and #f #t)', env))
    assert_equals("#t", interpret('(and #t #t)', env))

def test_xor():
    """test the logical 'exclusive or' operator"""
    assert_equals("#f", interpret('(xor #f #f)', env))
    assert_equals("#t", interpret('(xor #t #f)', env))
    assert_equals("#t", interpret('(xor #f #t)', env))
    assert_equals("#f", interpret('(xor #t #t)', env))

def test_greater_or_equal():
    """test the mathematical 'greater than or equal to' operator"""
    assert_equals("#f", interpret('(>= 1 2)', env))
    assert_equals("#t", interpret('(>= 2 2)', env))
    assert_equals("#t", interpret('(>= 2 1)', env))

def test_less_or_equal():
    """test the mathematical 'less than or equal to' operator"""
    assert_equals("#t", interpret('(<= 1 2)', env))
    assert_equals("#t", interpret('(<= 2 2)', env))
    assert_equals("#f", interpret('(<= 2 1)', env))

def test_less_than():
    """test the mathematical 'less than' operator"""
    assert_equals("#t", interpret('(< 1 2)', env))
    assert_equals("#f", interpret('(< 2 2)', env))
    assert_equals("#f", interpret('(< 2 1)', env))

def test_sum():
    """sum all of the elements in a list using the '+' operator"""
    assert_equals("5", interpret("(sum '(1 1 1 1 1))", env))
    assert_equals("10", interpret("(sum '(1 2 3 4))", env))
    assert_equals("0", interpret("(sum '())", env))

def test_length():
    """determine the length of a list"""
    assert_equals("5", interpret("(length '(1 2 3 4 5))", env))
    assert_equals("3", interpret("(length '(#t '(1 2 3) 'foo-bar))", env))
    assert_equals("0", interpret("(length '())", env))

def test_append():
    """'append' should combine two lists together, in the given order"""
    assert_equals("(1 2 3 4 5)", interpret("(append '(1 2) '(3 4 5))", env))
    assert_equals("(#t #f 'maybe)", interpret("(append '(#t) '(#f 'maybe))", env))
    assert_equals("()", interpret("(append '() '())", env))

def test_filter():
    """'filter' should apply a predicate to every element of a list and return only
    those elements that evaluate 'True'
    """
    interpret("""
        (define even
            (lambda (x)
                (eq (mod x 2) 0)))
    """, env)
    assert_equals("(2 4 6)", interpret("(filter even '(1 2 3 4 5 6))", env))

def test_map():
    """'map' creates a new list by applying a function to each element of another"""
    interpret("""
        (define inc
            (lambda (x) (+ 1 x)))
    """, env)
    assert_equals("(2 3 4)", interpret("(map inc '(1 2 3))", env))

def test_reverse():
    """create a list by 'reversing' the order of the elements of another"""
    assert_equals("(4 3 2 1)", interpret("(reverse '(1 2 3 4))", env))
    assert_equals("()", interpret("(reverse '())", env))

def test_range():
    """'range' creats a list of integers from 'start' to 'end'"""
    assert_equals("(1 2 3 4 5)", interpret("(range 1 5)", env))
    assert_equals("(1)", interpret("(range 1 1)", env))
    assert_equals("()", interpret("(range 2 1)", env))

def test_sort():
    """'sort' the elements of a list
    
    NOTE: This is a VERY naive, first pass sort.
          It will only sort short lists of integers.
    """
    assert_equals("(1 2 3 4 5 6 7)",
        interpret("(sort '(6 3 7 2 4 1 5))", env))
    assert_equals("()", interpret("'()", env))
