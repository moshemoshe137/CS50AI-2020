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
    board_list = sum(board, [])
    if (board_list.count(X) + board_list.count(O)) % 2 == 0:
        return X
    else:
        return O
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for row_num, row in enumerate(board):
        for col_num, col in enumerate(board[row_num]):
            if board[row_num][col_num] is EMPTY:
                possible_actions.add((row_num, col_num))
    return possible_actions
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Illegal move")

    new_board = copy.deepcopy(board)
    turn = player(board)
    action_row, action_col = action[0], action[1]
    new_board[action_row][action_col] = turn
    return new_board
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # check all rows
    for row in board:
        if all([row[0] == row[i] for i in range(3)]) and row[0] is not None:
            return row[0]

    # check all columns
    for col in range(3):
        if all([board[0][col] == board[i][col] for i in range(3)]) and board[0][col] is not None:
            return board[0][col]

    # check diagonals
    if all([board[0][0] == board[i][i] for i in range(3)]) and board[0][0] is not None:
        return board[0][0]
    if all([board[2][0] == board[2 - i][i] for i in range(3)]) and board[2][0] is not None:
        return board[2][0]
    return
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    elif len(actions(board)) == 0:
        return True

    return False
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    board_winner = winner(board)
    if board_winner == X:
        return 1
    elif board_winner is None:
        return 0
    else:
        return -1
    raise NotImplementedError


def max_value(board):
    if terminal(board):
        return utility(board)
    # thanks https://stackoverflow.com/questions/7781260/how-can-i-represent-an-infinite-number-in-python
    v = -float('inf')
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):
    if terminal(board):
        return utility(board)
    v = +float('inf')
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    player_turn = player(board)
    moves_d = {}
    for action in actions(board):
        if player_turn == X:
            moves_d[action] = min_value(result(board, action))
        else:
            moves_d[action] = max_value(result(board, action))

    best_option = max(moves_d.values()) if player_turn == X else min(moves_d.values())

    for action, value in moves_d.items():
        if value == best_option:
            return action
    raise NotImplementedError
