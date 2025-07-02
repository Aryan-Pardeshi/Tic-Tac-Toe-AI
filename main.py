import random

def new_board():
    return [[None, None, None] for _ in range(3)]

def render_board(board):
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

def make_move(board, x, y, player):
    if 0 <= x < 3 and 0 <= y < 3 and board[y][x] is None:
        board[y][x] = player
        return True
    print("Invalid move. Try again.")
    return False

def get_winner(board):
    
    lines = []
    # Add rows
    lines.extend(board)

    # Add columns
    for col in range(3):
        lines.append([board[row][col] for row in range(3)])

    # Add diagonals
    lines.append([board[i][i] for i in range(3)])
    lines.append([board[i][2 - i] for i in range(3)])
    for line in lines:
        if line[0] is not None and line[0] == line[1] == line[2]:
            return line[0]
    return None

def is_board_full(board):
    return all(cell is not None for row in board for cell in row)

def random_ai(board, player):
    empty_cells = [(x, y) for y in range(3) for x in range(3) if board[y][x] is None]
    return random.choice(empty_cells)

def finds_winning_moves_ai(board, current_player):
    for y in range(3):
        for x in range(3):
            if board[y][x] is None:
                board_copy = [row[:] for row in board]
                board_copy[y][x] = current_player
                if get_winner(board_copy) == current_player:
                    return (x, y)
    return random_ai(board, current_player)

def human_player(board, current_player):
    while True:
        try:
            print(f"Player '{current_player}', it's your turn!")
            x = int(input("Enter x coordinate (0-2): "))
            y = int(input("Enter y coordinate (0-2): "))
            if 0 <= x < 3 and 0 <= y < 3 and board[y][x] is None:
                return (x, y)
            print("Invalid move. That square is taken or out of bounds. Try again.\n")
        except ValueError:
            print("Please enter valid numbers between 0 and 2.\n")
            
def get_opponent(player):
    return 'O' if player == 'X' else 'X'
def get_legal_moves(board):
    moves = []
    for y in range(3):
        for x in range(3):
            if board[y][x] is None:
                moves.append((x, y))
    return moves

def minimax_score(board, current_player):
    winner = get_winner(board)
    if winner == 'X':
        return 10
    elif winner == 'O':
        return -10
    elif is_board_full(board):
        return 0

    moves = get_legal_moves(board)
    scores = []

    for move in moves:
        x, y = move
        new_board = [row[:] for row in board]
        new_board[y][x] = current_player

        score = minimax_score(new_board, get_opponent(current_player))
        scores.append(score)

    return max(scores) if current_player == 'X' else min(scores)

def minimax_ai(board, player):
    best_score = -float('inf') if player == 'X' else float('inf')
    best_move = None

    for move in get_legal_moves(board):
        x, y = move
        new_board = [row[:] for row in board]
        new_board[y][x] = player
        score = minimax_score(new_board, get_opponent(player))

        if (player == 'X' and score > best_score) or (player == 'O' and score < best_score):
            best_score = score
            best_move = move

    return best_move


def main():
    board = new_board()
    # Ask the player to choose 'X' or 'O'
    while True:
        player_choice = input("Do you want to be 'X' or 'O'? (X goes first): ").strip().upper()
        if player_choice in ['X', 'O']:
            break
        print("Invalid choice. Please enter 'X' or 'O'.\n")
    human = player_choice
    ai = 'O' if human == 'X' else 'X'
    current_player = 'X'

    print(f"Welcome to Tic Tac Toe! \nYou are player '{human}'")
    print("Here is the initial board:")
    print(render_board(board))

    while True:
        if current_player == human:
            x, y = human_player(board, human)
            make_move(board, x, y, human)
        else:
            x, y = minimax_ai(board, ai)
            make_move(board, x, y, ai)
        print(render_board(board))
        winner = get_winner(board)
        if winner:
            print(f"\n🎉 Player '{winner}' wins!")
            break
        if is_board_full(board):
            print("\nIt's a draw! The board is full.")
            break
        current_player = get_opponent(current_player)

if __name__ == '__main__':
    main()
