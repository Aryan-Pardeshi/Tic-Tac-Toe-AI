def new_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]

board = new_board()

def render_board(board):
    board_visual = f" {board[0][0]} | {board[0][1]} | {board[0][2]}\n {board[1][0]} | {board[1][1]} | {board[1][2]}\n {board[2][0]} | {board[2][1]} | {board[2][2]}"
    board_visual = board_visual.replace("None", " ")
    return board_visual
    
board[0][1] = "X"
board[1][1] = "O"
# Test the function
print(render_board(board))
