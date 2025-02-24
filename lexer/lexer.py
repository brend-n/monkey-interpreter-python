from typing import Optional


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
        self.read_char()  # Initialize first character

    def read_char(self) -> None:
        """Advance to and read the next character in the input."""
        if self._read_position >= len(self.source):
            self._current_char = None
        else:
            self._current_char = self.source[self._read_position]

        self._position = self._read_position
        self._read_position += 1
