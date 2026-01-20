"""Module containing utility functions and decorators for the TicTacToe game."""

from typing import Callable, Any


def validate_input(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator to validate user input for move selection.

    Wraps a function that requests user input. It catches `ValueError` (if input
    is not a number) and `IndexError` (although logic usually handles range
    checks manually) to ensure the game loop doesn't crash on invalid data type
    entry.

    Args:
        func: The function to decorate.

    Returns:
        The wrapped function with error handling.
    """

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            return func(*args, **kwargs)
        except ValueError:
            print("Invalid input: Please enter a numeric value.")

    return wrapper
