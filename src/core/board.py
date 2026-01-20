from src.config import Player


class Board:
    """Represents the game board and its state."""

    def __init__(self) -> None:
        """Initializes a new empty board."""
        self.grid = [Player.EMPTY.value] * 9

    def make_move(self, position: int, player_symbol: str) -> bool:
        """Attempts to place a player's token on the board.

        Args:
            position: The 0-indexed position on the board (0-8).
            player_symbol: The symbol of the player (e.g., 'X' or 'O').

        Returns:
            True if the move was successful, False otherwise (e.g., spot taken).
        """
        if 0 <= position < 9 and self.grid[position] == Player.EMPTY.value:
            self.grid[position] = player_symbol
            return True
        return False

    def check_winner(self, player_symbol: str) -> bool:
        """Checks if the specified player has won.

        Args:
            player_symbol: The symbol to check for a win condition.

        Returns:
            True if the player has a winning line, False otherwise.
        """
        win_conditions = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6),
        ]

        for a, b, c in win_conditions:
            if self.grid[a] == self.grid[b] == self.grid[c] == player_symbol:
                return True
        return False

    def is_full(self) -> bool:
        """Checks if the board is completely full.

        Returns:
            True if no empty spaces remain, False otherwise.
        """
        return Player.EMPTY.value not in self.grid

    def reset(self) -> None:
        """Resets the board to its initial empty state."""
        self.grid = [Player.EMPTY.value] * 9
