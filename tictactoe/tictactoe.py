"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None
board_count = 0

def get_board_count():
    global board_count
    return board_count

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def o_turn_state():
    """
    Returns starting state of the board.
    """
    return [[X, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def o_win_state():
    """
    Returns starting state of the board.
    """
    return [[X, O, EMPTY],
            [X, O, EMPTY],
            [EMPTY, EMPTY, X]]

def x_win_state():
    """
    Returns starting state of the board.
    """
    return [[O, X, X],
            [O, X, X],
            [EMPTY, O, EMPTY]]

def tie_state():
    """
    Returns starting state of the board.
    """
    return [[X, O, X],
            [O, X, O],
            [O, X, EMPTY]]

def o_pen_state():
    """
    Returns starting state of the board.
    """
    return [[X, O, X],
            [O, X, O],
            [EMPTY, X, EMPTY]]

def x_two_more_state():
    """
    Returns starting state of the board.
    """
    return [[X, O, X],
            [O, X, O],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # if it's an even number it's X turn
    play_count = 0
    for row in board:
        for item in row:
            if item != EMPTY:
                play_count += 1
    
    if play_count % 2 == 0:
        return X
    return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    i = 0
    for row in board:
        j = 0
        for item in row:
            if item == EMPTY:
                possible_actions.add((i,j))
            j += 1
        i += 1
    return possible_actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    global board_count 
    board_count += 1
    mut_board = copy.deepcopy(board)
    if mut_board[action[0]][action[1]] != EMPTY:
        raise Exception
    mut_board[action[0]][action[1]] = player(mut_board)
    return mut_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] == board[0][1] == board[0][2] != None:
        return board[0][0]
    elif board[1][0] == board[1][1] == board[1][2] != None:
        return board[1][0]
    elif board[2][0] == board[2][1] == board[2][2] != None:
        return board[2][0]
    elif board[0][0] == board[1][0] == board[2][0] != None:
        return board[0][0]
    elif board[0][1] == board[1][1] == board[2][1] != None:
        return board[0][1]
    elif board[0][2] == board[1][2] == board[2][2] != None:
        return board[0][2]
    elif board[0][0] == board[1][1] == board[2][2] != None:
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] != None:
        return board[0][2]
    return None
    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    for row in board:
        for item in row:
            if item == EMPTY:
                return False
    return True    




def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if board == None or board == 0:
        return 0
    if board == 1:
        return 1
    if board == -1:
        return -1
    result = winner(board)
    if result == X:
        return 1
    elif result == O:
        return -1
    else:
        return 0
    


def minimax(board):
    """
    Returns the optimal action for the current player on the board.

    I think I need to check which player I am and then either look for the min if I'm O or max if I'm X

    I get the available actions and then track either the min or the max for each possible action
    and then call the minimax for each action. It just keeps returning up the stack until we get a result
    and we return the best move with either the best min or max

    Given a state s

    The maximizing player picks action a in Actions(s) that produces the highest value of Min-Value(Result(s, a)).
    The minimizing player picks action a in Actions(s) that produces the lowest value of Max-Value(Result(s, a)).

    Function Min-Value(state):

    v = ∞

    if Terminal(state):

    return Utility(state)

    for action in Actions(state):

        v = Min(v, Max-Value(Result(state, action)))

    return v
    """
    plays = []
    if board == None or terminal(board):
        return None
    elif player(board) == X: #maximizing player
        for action in actions(board):
            plays.append([min_value(result(board,action)),action])
        return sorted(plays, key=lambda x: x[0], reverse=True)[0][1]
    else: #minimizing player
        for action in actions(board):
            plays.append([max_value(result(board,action)),action])
        return sorted(plays, key=lambda x: x[0])[0][1]

# Function Max-Value(state)

#     v = -∞

#     if Terminal(state):

#     ​ return Utility(state)

#     for action in Actions(state):

#     ​ v = Max(v, Min-Value(Result(state, action)))

#     return v
def max_value(board):
    value = -math.inf
    if terminal(board):
        return utility(board)
    # print(actions(board))
    for action in actions(board):
        value = max(value, min_value(result(board, action)))
        if value == 1:
            return 1
    return value

def min_value(board):
    value = math.inf
    if terminal(board):
        return utility(board)
    # print(actions(board))
    for action in actions(board):
        value = min(value, max_value(result(board, action)))
        if value == -1:
            return -1
    return value

# unit tests

