import random

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
    else:
        print("Invalid move. Try again.")
        return False

def get_winner(board):
    # List all possible lines (rows, columns, diagonals)
    lines = [
        # Rows
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        # Columns
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        # Diagonals
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    for line in lines:
        # print(line[0], line[1], line[2])
        if line[0] is not None and line[0] == line[1] == line[2]:
            return line[0]

    return None 
def is_board_full(board):
    for row in board:
        if None in row:
            return False
    return True

def random_ai(board, player):
    
    empty_cells = []
    for y in range(3):
        for x in range(3):
            if board[y][x] is None:
                empty_cells.append((x, y))
    return random.choice(empty_cells)


print("Welcome to Tic Tac Toe! \nYou are player 'X'")

print("Here is the initial board:")
print(render_board(board))

while True:
    # Player X move
    while True:
        print("\nPlayer 'X', it's your turn!")
        x = int(input("Enter x coordinate (0-2): "))
        y = int(input("Enter y coordinate (0-2): "))
        if make_move(x, y, "X"):
            break
    print(render_board(board))
    winner = get_winner(board)
    if winner:
        print(f"\n🎉 Player '{winner}' wins!")
        break
    if is_board_full(board):
        print("\nIt's a draw! The board is full.")
        break

    # Player O move
    # while True:
    #     print("\nPlayer 'O', it's your turn!")
    #     x = int(input("Enter x coordinate (0-2): "))
    #     y = int(input("Enter y coordinate (0-2): "))
    #     if make_move(x, y, "O"):
    #         break
    # print(render_board(board))
    # winner = get_winner(board)
    x, y = random_ai(board, 'O')
    make_move(x, y, 'O')
    if winner:
        print(f"\n🎉 Player '{winner}' wins!")
        break
    if is_board_full(board):
        print("\nIt's a draw! The board is full.")
        break

# ...existing code...
#Board[y][x] = "X" or "O"

# Example usage
# board[0][1] = "X"
# board[1][1] = "O"
#  Test the function
# print(render_board(board))

