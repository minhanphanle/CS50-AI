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
    countX = 0
    countO = 0

    if board == initial_state():
        return X

    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == X:
                countX += 1
            elif board[i][j] == O:
                countO += 1

    if countX == countO:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()

    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    board_cop = copy.deepcopy(board)

    if action in actions(board):
        board_cop[action[0]][action[1]] = player(board)
    else:
        raise ValueError('Action invalid.')

    return board_cop


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # check rows

    for i in range(0, 3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != EMPTY:
            return board[i][0]

    # check columns

    for i in range(0, 3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != EMPTY:
            return board[0][i]

    # check diagonals

    diagonal1 = set((board[0][0], board[1][1], board[2][2]))
    diagonal2 = set((board[2][0], board[1][1], board[0][2]))

    if len(diagonal1) == 1 or len(diagonal2) == 1 and board[1][1] != EMPTY:
        return board[1][1]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None or not actions(board):
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    def max_value(board, v_min=-100, alpha=-100, beta=100):

        best_action = None

        if terminal(board):
            return (utility(board), best_action)

        for action in actions(board):
            if min_value(result(board, action))[0] > v_min:
                v_min = min_value(result(board, action))[0]
                best_action = action
            if alpha < v_min:
                alpha = v_min
            if beta <= alpha:
                break

        return (v_min, best_action)

    def min_value(board, v_max=100, alpha=-100, beta=100):

        best_action = None

        if terminal(board):
            return (utility(board), best_action)

        for action in actions(board):
            if max_value(result(board, action))[0] < v_max:
                v_max = max_value(result(board, action))[0]
                best_action = action
            if beta > v_max:
                beta = v_max
            if beta <= alpha:
                break

        return (v_max, best_action)

    if player(board) == X:
        return max_value(board)[1]

    if player(board) == O:
        return min_value(board)[1]
