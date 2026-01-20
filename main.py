"""Entry point script for the TicTacToe game.

This script initializes and starts the game instance.
"""

from src.core.engine import TicTacToeGame

if __name__ == "__main__":
    game_instance = TicTacToeGame()
    game_instance.start()
