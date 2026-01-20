from src.config import Player, Difficulty
from .board import Board
from . import ai
from src.ui import render as ui


class TicTacToeGame:
    """Class representing the logic and state of a TicTacToe game."""

    def __init__(self) -> None:
        """Initializes the game with an empty board."""
        self.board = Board()
        self.player_name: str = "Player"
        self.difficulty: Difficulty = Difficulty.EASY

    def start(self) -> None:
        """Starts the main game loop."""
        ui.display_welcome()
        self.player_name = ui.get_player_name()
        self.difficulty = ui.get_difficulty(Difficulty)

        while True:
            game_ended = self._play_round()
            if game_ended:
                choice = ui.ask_restart()
                if choice == 0:
                    print("Thanks for playing! Goodbye.")
                    break

                self.board.reset()

                if choice == 2:
                    self.difficulty = ui.get_difficulty(Difficulty)

    def _play_round(self) -> bool:
        """Runs one full round of turns (Player then Computer).

        Returns:
            True if the game has ended (Win/Draw), False otherwise.
        """
        ui.print_board(self.board.grid)

        print(f"Your turn, {self.player_name}. Choose your position.")
        player_idx = ui.get_player_move(self.board.grid)
        self.board.grid[player_idx] = Player.CROSS.value

        if self.board.check_winner(Player.CROSS.value):
            ui.print_board(self.board.grid)
            print(f"{self.player_name} Wins! Computer Loses.")
            return True

        if self.board.is_full():
            ui.print_board(self.board.grid)
            print("It's a Draw!")
            return True

        comp_move = ai.get_computer_move(self.board.grid, self.difficulty)
        if comp_move != -1:
            self.board.grid[comp_move] = Player.CIRCLE.value

        if self.board.check_winner(Player.CIRCLE.value):
            ui.print_board(self.board.grid)
            print(f"Computer Wins! {self.player_name} Loses.")
            return True

        if self.board.is_full():
            ui.print_board(self.board.grid)
            print("It's a Draw!")
            return True

        return False
