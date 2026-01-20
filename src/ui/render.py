from typing import List
from .art import LOGO
from src.config import Player


def display_welcome():
    """Prints the game logo."""
    print(LOGO)


def get_player_name() -> str:
    """Prompts for player name."""
    raw_name = input("Enter the Player Name: ").strip()
    return raw_name.title() if raw_name else "Player"


def get_difficulty(difficulties) -> str:
    """Prompts for difficulty level."""
    print("Select Difficulty Level:")
    for idx, diff in enumerate(difficulties):
        print(f"{idx + 1}. {diff.value}")

    while True:
        try:
            choice_str = input("Enter number (1-4): ")
            choice = int(choice_str)
            if 1 <= choice <= len(difficulties):
                return list(difficulties)[choice - 1]
            print(f"Please enter a number between 1 and {len(difficulties)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def print_board(grid: List[str]) -> None:
    """Prints the current state of the game board to the console."""
    separator = "-" * 11
    row1 = f" {grid[6]} | {grid[7]} | {grid[8]} "
    row2 = f" {grid[3]} | {grid[4]} | {grid[5]} "
    row3 = f" {grid[0]} | {grid[1]} | {grid[2]} "

    print("\n" + separator)
    print(row1)
    print(separator)
    print(row2)
    print(separator)
    print(row3)
    print(separator + "\n")


def get_player_move(grid: List[str]) -> int:
    """Prompts the player for their move and validates it."""
    while True:
        try:
            choice_str = input("Enter a number (1-9): ")
            choice = int(choice_str)
            if 1 <= choice <= 9:
                if grid[choice - 1] == Player.EMPTY.value:
                    return choice - 1
                else:
                    print("That space is taken. Try again.")
            else:
                print("Please enter a number between 1 and 9.")
        except ValueError:
            print("That is not a valid number. Try again.")


def ask_restart() -> int:
    """Asks the user what they want to do next.

    Returns:
        0: Quit
        1: Restart
        2: Restart and Change Difficulty
    """
    while True:
        try:
            choice_str = input(
                "Type 1 to Restart, 0 to Quit, and 2 for change difficulty: "
            )
            choice = int(choice_str)
            if choice in [0, 1, 2]:
                return choice
            else:
                print("Please enter 0, 1, or 2.")
        except ValueError:
            print("Invalid input. Please enter a number (0, 1, or 2).")
