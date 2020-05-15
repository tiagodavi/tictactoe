"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    """
    Returns player who has the next turn on a board.
    """

    x, y = [], []

    for row in board:
        for column in row:
            if column == X:
                x.append(1)
            if column == O:
                y.append(1)

    if len(x) == len(y):
        return X
    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    result = set()

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] is EMPTY:
                result.add((i, j))

    return result 

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    row, column = action 

    if not isinstance(row , int) or not isinstance(column , int):
        raise Exception('Invalid Action')

    if board[row][column] is EMPTY:
        state = copy.deepcopy(board)
        turn = player(state)
        state[row][column] = turn
        return state
    else:
        raise Exception('Invalid Action')

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    total = len(board)
    result = set()

    for i in range(total):
        for j in range(len(board[i])):
            result.add((i,j,board[i][j]))

    left_values = []
    right_values = []

    for i in range(total):
        row_values = [value for (row, column, value) in result if row == i]
        won = has_winner(row_values)
        if won:
            return won

        column_values = [value for (row, column, value) in result if column == i]
        won = has_winner(column_values)
        if won:
            return won

        left = [value for (row, column, value) in result if row == i and column == i][0]
        right = [value for (row, column, value) in result if row == i and column == (total - i - 1)][0]
        
        left_values.append(left)
        right_values.append(right)

    won = has_winner(left_values)
    if won:
        return won

    won = has_winner(right_values)
    if won:
        return won

    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    won = winner(board)

    if won is not None:
        return True

    x = []

    for row in board:
        for column in row:
            if column is EMPTY:
                x.append(1)

    return len(x) == 0

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    result = winner(board)

    if result is X:
        return 1
    if result is O:
        return -1

    return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None

    turn = player(board)
    acts = actions(board)

    if turn is X:
        temp = []
        for a in acts:
            temp.append((min_value(result(board, a)), a))
        
        v = float("-inf") 
        a = None
        for i in range(len(temp)):
            x, y = temp[i]
            if x > v:
                v = x 
                a = y
        return a

    if turn is O:
        temp = []
        for a in acts:
            temp.append((max_value(result(board, a)), a))
        
        v = float("inf") 
        a = None
        for i in range(len(temp)):
            x, y = temp[i]
            if x < v:
               v = x 
               a = y
        return a

def max_value(board):
    if terminal(board):
        return utility(board)
    
    acts = actions(board)
    v = float("-inf")
    for a in acts:
        v = max(v, min_value(result(board, a)))

    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    
    acts = actions(board)
    v = float("inf")
    for a in acts:
        v = min(v, max_value(result(board, a)))
        
    return v

def has_winner(values):
    x = all([True if i is X else False for i in values])
    if x:
        return X

    o = all([True if i is O else False for i in values])
    if o:
        return O

    return None





