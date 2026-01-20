"""Configuration and Constants.

This module contains the global constants and enumerations used throughout the game.
"""

from enum import Enum


class Player(Enum):
    """Enum representing the players in the game."""

    CROSS = "X"
    CIRCLE = "O"
    EMPTY = " "


class Difficulty(Enum):
    """Enum representing the difficulty levels."""

    EASY = "Easy"
    NORMAL = "Normal"
    HARD = "Hard"
    HELL = "Hell"
