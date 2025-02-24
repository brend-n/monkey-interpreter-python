from enum import Enum


class TokenType(Enum):
    ILLEGAL = "ILLEGAL"
    EOF = "EOF"

    # Identifiers
    IDENT = "IDENT"
    INT = "INT"

    # Operators
    ASSIGN = "="
    PLUS = "+"
    MINUS = "-"
    BANG = "!"
    ASTERISK = "*"
    SLASH = "/"
    EQ = "=="
    NOT_EQ = "!="

    LT = "<"
    GT = ">"

    # Delimiters
    COMMA = ","
    SEMICOLON = ";"

    LPAREN = "("
    RPAREN = ")"
    LBRACE = "{"
    RBRACE = "}"

    # Keywords
    FUNCTION = "FUNCTION"
    RETURN = "RETURN"
    LET = "LET"
    IF = "IF"
    ELSE = "ELSE"
    TRUE = "TRUE"
    FALSE = "FALSE"


class Token():
    def __init__(self, type: TokenType, literal: str):
        self.type = type
        self.literal = literal


keywords = {
    "fn":     TokenType.FUNCTION,
    "return": TokenType.RETURN,
    "let":    TokenType.LET,
    "if":     TokenType.IF,
    "else":   TokenType.ELSE,
    "true":   TokenType.TRUE,
    "false":  TokenType.FALSE,
}


def LookupIdent(ident: str) -> TokenType:
    return keywords.get(ident, TokenType.IDENT)
