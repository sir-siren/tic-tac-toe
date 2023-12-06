import random
import sys
import time as tm

print(r'''
.___________. __    ______        .___________.    ___       ______        .___________.  ______    _______
|           ||  |  /      |       |           |   /   \     /      |       |           | /  __  \  |   ____|
`---|  |----`|  | |  ,----' ______`---|  |----`  /  ^  \   |  ,----' ______`---|  |----`|  |  |  | |  |__
    |  |     |  | |  |     |______|   |  |      /  /_\  \  |  |     |______|   |  |     |  |  |  | |   __|
    |  |     |  | |  `----.           |  |     /  _____  \ |  `----.           |  |     |  `--'  | |  |____
    |__|     |__|  \______|           |__|    /__/     \__\ \______|           |__|      \______/  |_______|

''')
nop = input("Enter the Player Name: ").title()
#create the board as a list of strings
board = [" " for i in range(9)]

def print_board():
    """
    Print the current board state.
    """
    row1 = " {} | {} | {} ".format(board[6], board[7], board[8])
    row2 = " {} | {} | {} ".format(board[3], board[4], board[5])
    row3 = " {} | {} | {} ".format(board[0], board[1], board[2])
    print()
    print("-"*11)
    print(row1)
    print("-"*11)
    print(row2)
    print("-"*11)
    print(row3)
    print("-"*11)
    print()

def is_victory(icon):
    """
    Check if the game is won by the given icon.

    Parameters:
    icon (str): The icon to check for victory.

    Returns:
    bool: True if the game is won, False otherwise.
    """
    #check rows
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
       (board[3] == icon and board[4] == icon and board[5] == icon) or \
       (board[6] == icon and board[7] == icon and board[8] == icon):
        return True
    #check columns
    elif (board[0] == icon and board[3] == icon and board[6] == icon) or \
         (board[1] == icon and board[4] == icon and board[7] == icon) or \
         (board[2] == icon and board[5] == icon and board[8] == icon):
        return True
    #check diagonals
    elif (board[0] == icon and board[4] == icon and board[8] == icon) or \
         (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False

def is_fail(icon):
    """
    Check if the game is lost by the given icon.

    Parameters:
    icon (str): The icon to check for loss.

    Returns:
    bool: True if the game is lost, False otherwise.
    """
    #check rows
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
       (board[3] == icon and board[4] == icon and board[5] == icon) or \
       (board[6] == icon and board[7] == icon and board[8] == icon):
        return False
    #check columns
    elif (board[0] == icon and board[3] == icon and board[6] == icon) or \
         (board[1] == icon and board[4] == icon and board[7] == icon) or \
         (board[2] == icon and board[5] == icon and board[8] == icon):
        return False
    #check diagonals
    elif (board[0] == icon and board[4] == icon and board[8] == icon) or \
         (board[2] == icon and board[4] == icon and board[6] == icon):
        return False
    else:
        return False

def is_draw():
    """
    Check if the game is a draw.

    Returns:
    bool: True if the game is a draw, False otherwise.
    """
    if " " not in board:
        return True
    else:
        return False

def player_turn(icon):
    """
    Perform the player's turn.

    Parameters:
    icon (str): The icon of the player.
    """
    print(f"Your turn, {nop}. Which space do you want to place your icon?")
    while True:
        try:
            choice = int(input("Enter a number (1-9): "))
        except ValueError:
            print("That's not a valid option. Try again.")
            continue
        if board[choice - 1] == " ":
            board[choice - 1] = icon
            break
        else:
            print("That space is taken. Try again.")

def computer_turn(icon):
    """
    Perform the computer's turn.

    Parameters:
    icon (str): The icon of the computer.
    """
    print("Computer is thinking...")
    tm.sleep(1)
    available_spaces = []
    for i, space in enumerate(board):
        if space == " ":
            available_spaces.append(i)
    choice = random.choice(available_spaces)
    board[choice] = icon

def clear_board():
    """
    Clear the board by resetting all spaces to empty.
    """
    global board
    board = [" " for i in range(9)]

def restart():
    """
    Restart the game or quit based on user input.
    """
    retry = int(input("Type 1 to Restart and 0 to Quit: "))
    if retry == 1:
        clear_board()
        game()
    elif retry == 0:
        print("Hope to see you soon!")
        sys.exit()
    else:
        print("Worng Input! Please try again!")
        restart()

def game():
    """
    The main game loop.
    """
    while True:
        print_board()
        player_turn("X")
        if is_victory("X"):
            print_board()
            print(f"{nop} Win! Computer Loses")
            restart()
        elif is_fail("X"):
            print(f"You {nop}! Computer Wins")
            restart()
        computer_turn("O")
        if is_victory("O"):
            print_board()
            print(f"Computer Wins! {nop} Lose!")
            restart()
        elif is_fail("O"):
            print(f"Computer You Lose! {nop} Wins!")
            restart()

game()
