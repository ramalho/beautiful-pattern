from typing import NewType, TypeAlias

from exceptions import UnexpectedCloseParen, UnexpectedEndOfSource

Symbol = NewType('Symbol', str)
Number: TypeAlias = int | float
Atom: TypeAlias = Number | Symbol
Expression: TypeAlias = Atom | list


def read(source: str) -> Expression:
    """Read a Scheme expression from a string."""
    return read_from_tokens(tokenize(source))


def tokenize(s: str) -> list[str]:
    """Convert a string into a list of tokens."""
    return s.replace('(', ' ( ').replace(')', ' ) ').split()


def read_from_tokens(tokens: list[str]) -> Expression:
    """Read an expression from a sequence of tokens."""
    if len(tokens) == 0:
        raise UnexpectedEndOfSource()
    token = tokens.pop(0)
    if '(' == token:
        exp = []
        while tokens and tokens[0] != ')':
            exp.append(read_from_tokens(tokens))
        if not tokens:
            raise UnexpectedEndOfSource()
        tokens.pop(0)  # discard ')'
        return exp
    elif ')' == token:
        raise UnexpectedCloseParen()
    else:
        return parse_atom(token)


def parse_atom(token: str) -> Atom:
    """Numbers become numbers; every other token is a symbol."""
    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            return Symbol(token)
