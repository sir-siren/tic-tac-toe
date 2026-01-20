import unittest

from src.config import Player
from src.core.board import Board


class TestBoard(unittest.TestCase):
    """Test suite for the Board class."""

    def setUp(self):
        """Create a fresh board before each test."""
        self.board = Board()

    def test_initial_state(self):
        """Test that the board is initialized correctly."""
        self.assertEqual(len(self.board.grid), 9)
        self.assertTrue(all(spot == Player.EMPTY.value for spot in self.board.grid))
        self.assertFalse(self.board.is_full())

    def test_make_move_valid(self):
        """Test making a valid move."""
        result = self.board.make_move(0, Player.CROSS.value)
        self.assertTrue(result)
        self.assertEqual(self.board.grid[0], Player.CROSS.value)

    def test_make_move_invalid_index(self):
        """Test making a move on an invalid index."""

        result = self.board.make_move(-1, Player.CROSS.value)
        self.assertFalse(result)

        result = self.board.make_move(9, Player.CROSS.value)
        self.assertFalse(result)

    def test_make_move_taken_spot(self):
        """Test attempting to move on an already occupied spot."""

        self.board.make_move(4, Player.CROSS.value)

        result = self.board.make_move(4, Player.CIRCLE.value)
        self.assertFalse(result)
        self.assertEqual(self.board.grid[4], Player.CROSS.value)

    def test_check_winner_rows(self):
        """Test winning conditions on rows."""

        self.board.grid[0] = self.board.grid[1] = self.board.grid[2] = (
            Player.CROSS.value
        )
        self.assertTrue(self.board.check_winner(Player.CROSS.value))

        self.board.reset()
        self.board.grid[6] = self.board.grid[7] = self.board.grid[8] = (
            Player.CIRCLE.value
        )
        self.assertTrue(self.board.check_winner(Player.CIRCLE.value))

    def test_check_winner_columns(self):
        """Test winning conditions on columns."""

        self.board.grid[0] = self.board.grid[3] = self.board.grid[6] = (
            Player.CROSS.value
        )
        self.assertTrue(self.board.check_winner(Player.CROSS.value))

    def test_check_winner_diagonals(self):
        """Test winning conditions on diagonals."""

        self.board.grid[0] = self.board.grid[4] = self.board.grid[8] = (
            Player.CROSS.value
        )
        self.assertTrue(self.board.check_winner(Player.CROSS.value))

        self.board.reset()
        self.board.grid[2] = self.board.grid[4] = self.board.grid[6] = (
            Player.CIRCLE.value
        )
        self.assertTrue(self.board.check_winner(Player.CIRCLE.value))

    def test_check_winner_no_winner(self):
        """Test that check_winner returns False when there is no winner."""
        self.board.grid = [
            Player.CROSS.value,
            Player.CIRCLE.value,
            Player.CROSS.value,
            Player.CIRCLE.value,
            Player.CROSS.value,
            Player.CIRCLE.value,
            Player.CIRCLE.value,
            Player.CROSS.value,
            Player.CIRCLE.value,
        ]
        self.assertFalse(self.board.check_winner(Player.CROSS.value))
        self.assertFalse(self.board.check_winner(Player.CIRCLE.value))

    def test_is_full(self):
        """Test is_full method."""

        self.board.grid = [Player.CROSS.value] * 8 + [Player.EMPTY.value]
        self.assertFalse(self.board.is_full())

        self.board.grid = [Player.CROSS.value] * 9
        self.assertTrue(self.board.is_full())

    def test_reset(self):
        """Test that reset clears the board."""
        self.board.make_move(0, Player.CROSS.value)
        self.board.reset()
        self.assertTrue(all(spot == Player.EMPTY.value for spot in self.board.grid))


if __name__ == "__main__":
    unittest.main()
