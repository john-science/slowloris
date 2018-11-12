from nose.tools import assert_equals, assert_raises
from slowloris.evaluator import evaluate
from slowloris.parser import parse, unparse
from slowloris.types import LispError
from slowloris.types import Closure, LispError, Environment


def test_decorator():
    """
    Tests that decorator feature works
    """

    # deco = """
    # (def some_decor
    # (lambda (n)
    #     (+ n 1)))
    # """
    # env = Environment()
    # closure = evaluate(parse(deco), env)
    #
    # program = """
    #  (@some_decor
    #  (def cube
    #  (lambda (n)
    #      (* n n n))))
    #
    #  """
    # expected_ast = ['@some_decor',
    #                 ['def', 'cube', ['lambda', ['n'], ['*', 'n', 'n', 'n']]]]

    # parsed_program = parse(program)
    # assert_equals(expected_ast, parsed_program)
    # #
    # evaluate(parsed_program, env)
    program1 = """
    (def inc
    (lambda (n)
        (+ n 1)))
    """
    program2 = """(@inc
    (def power_2
    (lambda (n)
        (* n n)))
        )
    """
    env = Environment()
    first_ast = parse(program1)
    second_ast = parse(program2)
    first_closure = evaluate(first_ast, env)
    second_closure = evaluate(second_ast, env)

    third_ast = parse("(power_2 3)")
    assert_equals(10, evaluate(third_ast, env))


test_decorator()