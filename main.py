def new_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]

board = new_board()

def render_board(board):
    # Replace None with space for display
    b = [[cell if cell is not None else " " for cell in row] for row in board]
    board_visual = (
        "  0 1 2\n"
        "  ------\n"
        f"0|{b[0][0]} {b[0][1]} {b[0][2]}|\n"
        f"1|{b[1][0]} {b[1][1]} {b[1][2]}|\n"
        f"2|{b[2][0]} {b[2][1]} {b[2][2]}|\n"
        "  ------"
    )
    return board_visual

def make_move(x, y, player):
    if 0 <= x < 3 and 0 <= y < 3 and board[y][x] is None:
        board[y][x] = player
        return True
    return False

x = int(input("Enter x coordinate (0-2): "))
y = int(input("Enter y coordinate (0-2): "))

print(make_move(x, y, "X"))

print(make_move(1, 1, "O"))  # Example move for player "O"
# ...existing code...
#Board[y][x] = "X" or "O"

# Example usage
board[0][1] = "X"
board[1][1] = "O"
# Test the function
print(render_board(board))

