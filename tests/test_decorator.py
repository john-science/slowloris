from nose.tools import assert_equals, assert_raises
from slowloris.evaluator import evaluate
from slowloris.parser import parse
from slowloris.types import Environment, LispError


def test_decorator():
    """
    Simple test case of decorator
    """
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
    evaluate(first_ast, env)
    evaluate(second_ast, env)

    third_ast = parse("(power_2 3)")
    assert_equals(10, evaluate(third_ast, env))


def test_undefined_decorator():

    program2 = """(@inc
    (def power_2
    (lambda (n)
        (* n n)))
        )
    """

    env = Environment()
    second_ast = parse(program2)
    evaluate(second_ast, env)
    third_ast = parse("(power_2 3)")
    with assert_raises(LispError):
        assert_equals(10, evaluate(third_ast, env))

