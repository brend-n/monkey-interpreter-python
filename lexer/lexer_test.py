import pytest
from .lexer import Lexer
from monkey_token.token import Token, TokenType


@pytest.mark.parametrize("input,expected_tokens", [
    ("=+(){},;", [
        Token(TokenType.ASSIGN, "="),
        Token(TokenType.PLUS, "+"),
        Token(TokenType.LEFT_PAREN, "("),
        Token(TokenType.RIGHT_PAREN, ")"),
        Token(TokenType.LEFT_BRACE, "{"),
        Token(TokenType.RIGHT_BRACE, "}"),
        Token(TokenType.COMMA, ","),
        Token(TokenType.SEMICOLON, ";"),
    ]),
])
def test_next_token(input, expected_tokens):
    lex = Lexer(input)
    for x in expected_tokens:
        a = lex.next_token()
        assert a == x
