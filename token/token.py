from enum import Enum
from typing import Dict


class TokenType(Enum):
    # Special tokens
    ILLEGAL = "ILLEGAL"
    EOF = "EOF"

    # Identifiers and literals
    IDENTIFIER = "IDENTIFIER"
    INTEGER = "INTEGER"

    # Operators
    ASSIGN = "="
    PLUS = "+"
    MINUS = "-"
    BANG = "!"
    ASTERISK = "*"
    SLASH = "/"
    EQUALS = "=="
    NOT_EQUALS = "!="
    LESS_THAN = "<"
    GREATER_THAN = ">"

    # Delimiters
    COMMA = ","
    SEMICOLON = ";"
    LEFT_PAREN = "("
    RIGHT_PAREN = ")"
    LEFT_BRACE = "{"
    RIGHT_BRACE = "}"

    # Keywords
    FUNCTION = "FUNCTION"
    RETURN = "RETURN"
    LET = "LET"
    IF = "IF"
    ELSE = "ELSE"
    TRUE = "TRUE"
    FALSE = "FALSE"


class Token:
    """Represents a token in the programming language."""

    def __init__(self, token_type: TokenType, literal: str):
        """Initialize a new token.

        Args:
            token_type: The type of the token
            literal: The literal string value of the token
        """
        self.type = token_type
        self.literal = literal


# Mapping of keywords to their corresponding token types
KEYWORDS: Dict[str, TokenType] = {
    "fn": TokenType.FUNCTION,
    "return": TokenType.RETURN,
    "let": TokenType.LET,
    "if": TokenType.IF,
    "else": TokenType.ELSE,
    "true": TokenType.TRUE,
    "false": TokenType.FALSE,
}


def lookup_identifier(identifier: str) -> TokenType:
    """Look up an identifier and return its token type.

    Args:
        identifier: The identifier string to look up

    Returns:
        The corresponding token type for keywords,
        or TokenType.IDENTIFIER for other identifiers
    """
    return KEYWORDS.get(identifier, TokenType.IDENTIFIER)
