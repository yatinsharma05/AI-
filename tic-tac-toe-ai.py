import math

# Constants
PLAYER = 'X'
AI = 'O'
EMPTY = ' '

# Print the board
def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

# Check for a winner
def check_winner(board, player):
    # Check rows, columns and diagonals
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]]
    ]
    if [player, player, player] in win_conditions:
        return True
    return False

# Check for a draw
def check_draw(board):
    for row in board:
        if EMPTY in row:
            return False
    return True

# Get all available moves
def get_available_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                moves.append((i, j))
    return moves

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    if check_winner(board, AI):
        return 1
    if check_winner(board, PLAYER):
        return -1
    if check_draw(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for move in get_available_moves(board):
            board[move[0]][move[1]] = AI
            score = minimax(board, depth + 1, False)
            board[move[0]][move[1]] = EMPTY
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in get_available_moves(board):
            board[move[0]][move[1]] = PLAYER
            score = minimax(board, depth + 1, True)
            board[move[0]][move[1]] = EMPTY
            best_score = min(score, best_score)
        return best_score

# AI move
def ai_move(board):
    best_score = -math.inf
    best_move = None
    for move in get_available_moves(board):
        board[move[0]][move[1]] = AI
        score = minimax(board, 0, False)
        board[move[0]][move[1]] = EMPTY
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

# Main game loop
def main():
    board = [[EMPTY for _ in range(3)] for _ in range(3)]
    print("Tic Tac Toe Game!")
    print_board(board)

    while True:
        # Player move
        row, col = map(int, input("Enter your move (row and column): ").split())
        if board[row][col] != EMPTY:
            print("Invalid move! Try again.")
            continue
        board[row][col] = PLAYER

        if check_winner(board, PLAYER):
            print_board(board)
            print("Player wins!")
            break
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # AI move
        move = ai_move(board)
        board[move[0]][move[1]] = AI

        print_board(board)

        if check_winner(board, AI):
            print("AI wins!")
            break
        if check_draw(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
