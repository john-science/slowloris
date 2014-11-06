# -*- coding: utf-8 -*-

from nose.tools import assert_equals
from os.path import dirname, relpath, join

from slowloris.interpreter import interpret, interpret_file
from slowloris.types import Environment

env = Environment()
path = join(dirname(relpath(__file__)), '..', 'stdlib', 'stdlib.sl')
interpret_file(path, env)

"""
The standard library is implemented in the file `stdlib.sl` in the
Slow Loris root directory.

Anything inside `stdlib.sl` is also available from the REPL, so feel
free to test things out there.

    $ ./repl
    →  (not True)
    False
"""

def test_not():
    """logical operator 'not' should return opposite of given boolean value"""
    assert_equals("True", interpret('(not False)', env))
    assert_equals("False", interpret('(not True)', env))

def test_or():
    """test the logical 'or' operator"""
    assert_equals("False", interpret('(or False False)', env))
    assert_equals("True", interpret('(or True False)', env))
    assert_equals("True", interpret('(or False True)', env))
    assert_equals("True", interpret('(or True True)', env))

def test_and():
    """test the logical 'and' operator"""
    assert_equals("False", interpret('(and False False)', env))
    assert_equals("False", interpret('(and True False)', env))
    assert_equals("False", interpret('(and False True)', env))
    assert_equals("True", interpret('(and True True)', env))

def test_xor():
    """test the logical 'exclusive or' operator"""
    assert_equals("False", interpret('(xor False False)', env))
    assert_equals("True", interpret('(xor True False)', env))
    assert_equals("True", interpret('(xor False True)', env))
    assert_equals("False", interpret('(xor True True)', env))

def test_greater_or_equal():
    """test the mathematical 'greater than or equal to' operator"""
    assert_equals("False", interpret('(>= 1 2)', env))
    assert_equals("True", interpret('(>= 2 2)', env))
    assert_equals("True", interpret('(>= 2 1)', env))

def test_less_or_equal():
    """test the mathematical 'less than or equal to' operator"""
    assert_equals("True", interpret('(<= 1 2)', env))
    assert_equals("True", interpret('(<= 1.1 2.0)', env))
    assert_equals("True", interpret('(<= 1.75 2)', env))
    assert_equals("True", interpret('(<= 2 2)', env))
    assert_equals("False", interpret('(<= 2 1)', env))

def test_less_than():
    """test the mathematical 'less than' operator"""
    assert_equals("True", interpret('(< 1 2)', env))
    assert_equals("False", interpret('(< 2 2)', env))
    assert_equals("False", interpret('(< 2 1)', env))

def test_sum():
    """sum all of the elements in a list using the '+' operator"""
    assert_equals("5", interpret("(sum '(1 1 1 1 1))", env))
    assert_equals("6.5", interpret("(sum '(1.1 1.2 1.3 1.4 1.5))", env))
    assert_equals("10", interpret("(sum '(1 2 3 4))", env))
    assert_equals("0", interpret("(sum '())", env))

def test_length():
    """determine the length of a list"""
    assert_equals("5", interpret("(length '(1 2 3 4 5))", env))
    assert_equals("3", interpret("(length '(True '(1 2 3) 'foo-bar))", env))
    assert_equals("0", interpret("(length '())", env))

def test_append():
    """'append' should combine two lists together, in the given order"""
    assert_equals("(1 2 3 4 5)", interpret("(append '(1 2) '(3 4 5))", env))
    assert_equals("(True False 'maybe)", interpret("(append '(True) '(False 'maybe))", env))
    assert_equals("()", interpret("(append '() '())", env))

def test_filter():
    """'filter' should apply a predicate to every element of a list and return only
    those elements that evaluate 'True'
    """
    interpret("""
        (def even
            (lambda (x)
                (eq (mod x 2) 0)))
    """, env)
    assert_equals("(2 4 6)", interpret("(filter even '(1 2 3 4 5 6))", env))

def test_map():
    """'map' creates a new list by applying a function to each element of another"""
    interpret("""
        (def inc
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

def test_range_step():
    """'range-step' creats a list of integers from 'start' to 'end'"""
    assert_equals("(1 5 9 13)", interpret("(range-step 1 15 4)", env))
    assert_equals("(1)", interpret("(range-step 1 1 1)", env))
    assert_equals("()", interpret("(range-step 2 1 1)", env))

def test_quick_sort():
    """'quick-sort' the elements of a list
    
    A simple implementation for quick sort on a linked list of numbers.
    """
    assert_equals("(1 2 3 4 5 6 7)",
        interpret("(quick-sort '(6 3 7 2 4 1 5))", env))
    assert_equals("()", interpret("'()", env))

def test_insert_sort():
    """'insert-sort' the elements of a list
    
    A simple implementation for insert sort on a linked list of numbers.
    """
    assert_equals("(1 2 3 4 5 6 7)",
        interpret("(insert-sort '(6 3 7 2 4 1 5))", env))
    assert_equals("()", interpret("'()", env))

def test_str_append():
    """'str_append' two strings to create a new string
    """
    assert_equals('"hello world"', interpret('(str_append "hello " "world")'))
    assert_equals('"#loveyou"', interpret('(str_append "#" "loveyou")'))

def test_str_split():
    """'str_split' a string into a list of strings
    """
    assert_equals("'" + '("slow" "loris" "is" "almost" "a" "language")',
        interpret('(str_split "slow loris is almost a language" " ")'))
    assert_equals("'" + '("rock" "lobster" "dinner")',
        interpret('(str_split "rock lobster dinner" " ")'))
