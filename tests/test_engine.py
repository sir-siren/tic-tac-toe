import unittest
from unittest.mock import MagicMock, patch

from src.config import Difficulty, Player
from src.core.engine import TicTacToeGame


class TestEngine(unittest.TestCase):
    """Test suite for the Game Engine."""

    def setUp(self):
        self.game = TicTacToeGame()

    @patch("src.core.engine.ui")
    def test_start_flow_quit_immediately(self, mock_ui):
        """Test that the game starts and quits if user chooses to quit."""

        mock_ui.get_player_name.return_value = "Tester"
        mock_ui.get_difficulty.return_value = Difficulty.EASY

        with patch.object(self.game, "_play_round", return_value=True) as mock_play:
            mock_ui.ask_restart.return_value = 0

            self.game.start()

            mock_ui.display_welcome.assert_called_once()
            mock_play.assert_called_once()
            mock_ui.ask_restart.assert_called_once()

    @patch("src.core.engine.ui")
    def test_play_round_player_wins(self, mock_ui):
        """Test a round where the player wins."""

        self.game.board.check_winner = MagicMock(side_effect=[True])
        self.game.board.grid = [Player.EMPTY.value] * 9

        mock_ui.get_player_move.return_value = 0

        result = self.game._play_round()

        self.assertTrue(result)
        self.game.board.check_winner.assert_called_with(Player.CROSS.value)

        self.assertTrue(mock_ui.print_board.called)

    @patch("src.core.engine.ai")
    @patch("src.core.engine.ui")
    def test_play_round_computer_wins(self, mock_ui, mock_ai):
        """Test a round where computer wins."""

        self.game.board.check_winner = MagicMock(side_effect=[False, True])
        self.game.board.is_full = MagicMock(return_value=False)
        self.game.board.grid = [Player.EMPTY.value] * 9

        mock_ui.get_player_move.return_value = 0
        mock_ai.get_computer_move.return_value = 1

        result = self.game._play_round()

        self.assertTrue(result)

        self.assertEqual(self.game.board.check_winner.call_count, 2)
        mock_ai.get_computer_move.assert_called_once()


if __name__ == "__main__":
    unittest.main()
