import unittest
from unittest.mock import patch

from src.config import Difficulty, Player
from src.core import ai


class TestAI(unittest.TestCase):
    """Test suite for the AI logic (Minimax and Heuristics)."""

    def test_get_computer_move_no_moves(self):
        """Test that -1 is returned when no moves are available."""
        full_grid = [Player.CROSS.value] * 9
        move = ai.get_computer_move(full_grid, Difficulty.HARD)
        self.assertEqual(move, -1)

    def test_easy_difficulty_randomness(self):
        """Test that Easy difficulty picks a valid random move."""
        grid = [Player.EMPTY.value] * 9
        with patch("random.choice", return_value=4):
            move = ai.get_computer_move(grid, Difficulty.EASY)
            self.assertEqual(move, 4)

    def test_normal_difficulty_blocking(self):
        """Test that Normal difficulty blocks an immediate win."""

        grid = [
            Player.CROSS.value,
            Player.CROSS.value,
            Player.EMPTY.value,
            Player.EMPTY.value,
            Player.EMPTY.value,
            Player.EMPTY.value,
            Player.EMPTY.value,
            Player.EMPTY.value,
            Player.EMPTY.value,
        ]
        move = ai.get_computer_move(grid, Difficulty.NORMAL)
        self.assertEqual(move, 2)

    def test_hard_difficulty_minimax_win(self):
        """Test that Hard difficulty finds a winning move."""

        grid = [
            Player.CROSS.value,
            Player.CROSS.value,
            Player.EMPTY.value,
            Player.CIRCLE.value,
            Player.CIRCLE.value,
            Player.EMPTY.value,
            Player.EMPTY.value,
            Player.EMPTY.value,
            Player.EMPTY.value,
        ]

        with patch("random.random", return_value=1.0):
            move = ai.get_computer_move(grid, Difficulty.HARD)
        self.assertEqual(move, 5)

    def test_minimax_prevents_loss(self):
        """Verify Minimax algorithm finds the optimal move to prevent loss."""

        grid = [
            Player.CROSS.value,
            Player.EMPTY.value,
            Player.CROSS.value,
            Player.EMPTY.value,
            Player.CIRCLE.value,
            Player.EMPTY.value,
            Player.EMPTY.value,
            Player.EMPTY.value,
            Player.EMPTY.value,
        ]

        with patch("random.random", return_value=1.0):
            move = ai.get_computer_move(grid, Difficulty.HELL)
        self.assertEqual(move, 1)

    def test_check_winner_sim(self):
        """Test the Simulation Winner Check helper."""

        grid = [
            Player.CROSS.value,
            Player.CROSS.value,
            Player.CROSS.value,
            Player.EMPTY.value,
            Player.EMPTY.value,
            Player.EMPTY.value,
            Player.EMPTY.value,
            Player.EMPTY.value,
            Player.EMPTY.value,
        ]
        self.assertTrue(ai._check_winner_sim(grid, Player.CROSS.value))
        self.assertFalse(ai._check_winner_sim(grid, Player.CIRCLE.value))


if __name__ == "__main__":
    unittest.main()
