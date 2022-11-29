from pytest import mark

from parser import parse, Expression


@mark.parametrize(
    'source, expected',
    [
        ('7', 7),
        ('x', 'x'),
        ('(sum 1 2 3)', ['sum', 1, 2, 3]),
        ('(+ (* 2 100) (* 1 10))', ['+', ['*', 2, 100], ['*', 1, 10]]),
        ('99 100', 99),  # parse stops at the first complete expression
        ('(a)(b)', ['a']),
    ],
)
def test_parse(source: str, expected: Expression) -> None:
    got = parse(source)
    assert got == expected
