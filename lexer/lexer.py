from typing import Optional
from monkey_token.token import Token, TokenType


class Lexer:
    """A lexical analyzer that processes input text character by character."""

    def __init__(self, source: str) -> None:
        """Initialize the lexer with source text.

        Args:
            source: The input text to be analyzed
        """
        self.source = source
        self._position: int = 0
        self._read_position: int = 0
        self._current_char: Optional[str] = None
        self.__read_char()  # Initialize first character

    def __read_char(self) -> None:
        """Advance to and read the next character in the input."""
        if self._read_position >= len(self.source):
            self._current_char = None
        else:
            self._current_char = self.source[self._read_position]

        self._position = self._read_position
        self._read_position += 1

    def __consumeWhitespace(self) -> None:
        """Advances input to next non-whitespace character"""
        while self._current_char in [' ', '\t', '\n', '\r']:
            self.__read_char()

    def next_token(self) -> Token:
        """
        Returns the next token in the input stream, advancing the character
        pointer.

        This method consumes whitespace and returns a Token object based on
        the current character. It handles single-character tokens like
        operators and delimiters.

        Returns:
            Token: A Token object containing:
                - TokenType: The type of token
                - str: The literal string value of the token
        """

        self.__consumeWhitespace()

        tok = Token(TokenType.ILLEGAL, "")

        # switch on the current character
        match self._current_char:
            case "=":
                tok = Token(TokenType.ASSIGN, "=")
            case "+":
                tok = Token(TokenType.PLUS, "+")
            case "(":
                tok = Token(TokenType.LEFT_PAREN, "(")
            case ")":
                tok = Token(TokenType.RIGHT_PAREN, ")")
            case "{":
                tok = Token(TokenType.LEFT_BRACE, "{")
            case "}":
                tok = Token(TokenType.RIGHT_BRACE, "}")
            case ",":
                tok = Token(TokenType.COMMA, ",")
            case ";":
                tok = Token(TokenType.SEMICOLON, ";")

        self.__read_char()

        return tok
