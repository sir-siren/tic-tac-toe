import random
import time
from typing import List
from src.config import Player, Difficulty


def get_computer_move(board_grid: List[str], difficulty: Difficulty) -> int:
    """Determines the computer's move based on difficulty level.

    Args:
        board_grid: The current state of the board.
        difficulty: The selected difficulty level.

    Returns:
        The index of the chosen move, or -1 if no moves available.
    """
    print(f"Computer is thinking ({difficulty.value})...")
    time.sleep(0.5)

    available_indices = [
        i for i, spot in enumerate(board_grid) if spot == Player.EMPTY.value
    ]
    if not available_indices:
        return -1

    if difficulty == Difficulty.EASY:
        return random.choice(available_indices)

    if difficulty == Difficulty.NORMAL:
        move = _find_best_immediate_move(board_grid, available_indices)
        if move != -1:
            return move
        return random.choice(available_indices)

    if difficulty == Difficulty.HARD:
        if random.random() < 0.2:
            return random.choice(available_indices)

    if difficulty == Difficulty.HELL:
        if random.random() < 0.05:
            return random.choice(available_indices)

    best_score = -float("inf")
    best_move = -1

    for move in available_indices:
        board_grid[move] = Player.CIRCLE.value
        score = _minimax(board_grid, 0, False)
        board_grid[move] = Player.EMPTY.value
        if score > best_score:
            best_score = score
            best_move = move

    return best_move if best_move != -1 else random.choice(available_indices)


def _find_best_immediate_move(grid: List[str], available: List[int]) -> int:
    """Checks for winning moves or blocking moves."""
    for move in available:
        grid[move] = Player.CIRCLE.value
        if _check_winner_sim(grid, Player.CIRCLE.value):
            grid[move] = Player.EMPTY.value
            return move
        grid[move] = Player.EMPTY.value

    for move in available:
        grid[move] = Player.CROSS.value
        if _check_winner_sim(grid, Player.CROSS.value):
            grid[move] = Player.EMPTY.value
            return move
        grid[move] = Player.EMPTY.value

    return -1


def _minimax(grid: List[str], depth: int, is_maximizing: bool) -> int:
    """Minimax algorithm for perfect play."""
    if _check_winner_sim(grid, Player.CIRCLE.value):
        return 10 - depth
    if _check_winner_sim(grid, Player.CROSS.value):
        return depth - 10
    if Player.EMPTY.value not in grid:
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for i, val in enumerate(grid):
            if val == Player.EMPTY.value:
                grid[i] = Player.CIRCLE.value
                score = _minimax(grid, depth + 1, False)
                grid[i] = Player.EMPTY.value
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i, val in enumerate(grid):
            if val == Player.EMPTY.value:
                grid[i] = Player.CROSS.value
                score = _minimax(grid, depth + 1, True)
                grid[i] = Player.EMPTY.value
                best_score = min(score, best_score)
        return best_score


def _check_winner_sim(grid: List[str], icon: str) -> bool:
    """Helper to check win condition on a simulated board list."""
    if (
        (grid[0] == grid[1] == grid[2] == icon)
        or (grid[3] == grid[4] == grid[5] == icon)
        or (grid[6] == grid[7] == grid[8] == icon)
    ):
        return True
    if (
        (grid[0] == grid[3] == grid[6] == icon)
        or (grid[1] == grid[4] == grid[7] == icon)
        or (grid[2] == grid[5] == grid[8] == icon)
    ):
        return True
    if (grid[0] == grid[4] == grid[8] == icon) or (
        grid[2] == grid[4] == grid[6] == icon
    ):
        return True
    return False
