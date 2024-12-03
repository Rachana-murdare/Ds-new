# Tic-Tac-Toe Game in Python

def print_board(board):
    """Prints the Tic-Tac-Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def is_winner(board, player):
    """Checks if the given player has won."""
    # Check rows, columns, and diagonals
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_draw(board):
    """Checks if the game is a draw."""
    return all(cell != " " for row in board for cell in row)


def get_move(board, player):
    """Prompts the player to make a move."""
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] == " ":
                return row, col
            else:
                print("Cell already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Enter a number between 1 and 9.")


def tic_tac_toe():
    """Main function to play the game."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        row, col = get_move(board, players[current_player])
        board[row][col] = players[current_player]
        print_board(board)

        if is_winner(board, players[current_player]):
            print(f"Congratulations! Player {players[current_player]} wins!")
            break

        if is_draw(board):
            print("It's a draw!")
            break

        current_player = 1 - current_player


if __name__ == "__main__":
    tic_tac_toe()
