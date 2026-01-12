#!/usr/bin/python3
# Code provided by Holberton School

def print_board(board):
    """Print the current state of the board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """Check if there is a winner."""
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    """Main function to play the game."""
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))

            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Invalid input. Row and column must be 0, 1, or 2.")
                continue

            if board[row][col] == " ":
                board[row][col] = player
                if check_winner(board):
                    print_board(board)
                    print("Player " + player + " wins!")
                    break
                player = "O" if player == "X" else "X"
            else:
                print("That spot is already taken! Try again.")
        except ValueError:
            print("Invalid input. Please enter numeric values for row and column.")

if __name__ == "__main__":
    tic_tac_toe()

# Previous errors:
# 1. No validation for user input, causing crashes on invalid input.
# 2. Incorrect winner announcement due to player switch after a win.
#
# Fixes:
# 1. Added input validation to ensure row and column are within range.
# 2. Corrected winner announcement by breaking the loop immediately after a win.
#
# Expected behavior:
# The game runs smoothly, handles invalid inputs gracefully, and announces the correct winner.