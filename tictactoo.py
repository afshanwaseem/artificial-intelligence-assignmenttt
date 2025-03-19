import math

X = "X"
O = "O"
EMPTY = None

def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    return X if x_count <= o_count else O

def actions(board):
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}

def result(board, action):
    i, j = action
    if board[i][j] is not EMPTY:
        raise ValueError("Invalid action")
    new_board = [row[:] for row in board]
    new_board[i][j] = player(board)
    return new_board

def winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not EMPTY:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2]
    return None

def terminal(board):
    return winner(board) is not None or all(cell is not EMPTY for row in board for cell in row)

def utility(board):
    win = winner(board)
    return 1 if win == X else -1 if win == O else 0

def minimax(board):
    if terminal(board):
        return None
    
    def max_value(board):
        if terminal(board):
            return utility(board), None
        v, best_move = -math.inf, None
        for action in actions(board):
            min_val, _ = min_value(result(board, action))
            if min_val > v:
                v, best_move = min_val, action
        return v, best_move

    def min_value(board):
        if terminal(board):
            return utility(board), None
        v, best_move = math.inf, None
        for action in actions(board):
            max_val, _ = max_value(result(board, action))
            if max_val < v:
                v, best_move = max_val, action
        return v, best_move

    current_player = player(board)
    return max_value(board)[1] if current_player == X else min_value(board)[1]