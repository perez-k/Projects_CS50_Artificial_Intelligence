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
    # Count the number of X and number of O in board
    xc = board[0].count(X) + board[1].count(X) + board[2].count(X)
    oc = board[0].count(O) + board[1].count(O) + board[2].count(O)

    if xc == 0 and oc == 0:
        return X

    elif xc > oc:
        return O

    elif xc == oc:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # An empty set
    s = set()

    # For each line
    for i in range (3):
        # For each column ( cell )
        for j in range (3):
            # If the user can play there
            if board[i][j] == EMPTY:
                s.add((i, j))

    return s



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    b = copy.deepcopy(board)

    # Count the number of X and number of O in board
    xc = board[0].count(X) + board[1].count(X) + board[2].count(X)
    oc = board[0].count(O) + board[1].count(O) + board[2].count(O)

    if xc == 0 and oc == 0:
        b[action[0]] [action[1]] = X

    elif xc > oc:
        b[action[0]] [action[1]] = O

    elif xc == oc:
        b[action[0]] [action[1]] = X

    return b


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    bd = copy.deepcopy(board)

    # Determine if X won
    # 3 of X moves in a row horizontally
    for i in range (3):
        if bd[i].count(X) == 3:
             return X
    # 3 of X moves in a row vertically
    for j in range(3):
        if bd[0][j] == bd[1][j] == bd[2][j] == X:
            return X
    # 3 of X moves in a row diagonally
    if bd[0][0] == bd[1][1] == bd[2][2] == X:
        return X
    elif bd[0][2] == bd[1][1] == bd[2][0] == X:
        return X


    # Determine if O won
    # 3 of O moves in a row horizontally
    for i in range (3):
        if bd[i].count(O) == 3:
             return O
    # 3 of O moves in a row vertically
    for j in range(3):
        if bd[0][j] == bd[1][j] == bd[2][j] == O:
            return O
    # 3 of O moves in a row diagonally
    if bd[0][0] == bd[1][1] == bd[2][2] == O:
        return O
    elif bd[0][2] == bd[1][1] == bd[2][0] == O:
        return O

    # No Winner
    return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    bd = copy.deepcopy(board)

    # Determine if someone has won
    # 3 of X or O moves in a row horizontally
    for i in range (3):
        if bd[i].count(X) == 3 or bd[i].count(O) == 3:
             return True
    # 3 of X or O moves in a row vertically
    for j in range(3):
        if bd[0][j] == bd[1][j] == bd[2][j] != EMPTY:
            return True
    # 3 of X or O moves in a row diagonally
    if bd[0][0] == bd[1][1] == bd[2][2] != EMPTY:
        return True
    elif bd[0][2] == bd[1][1] == bd[2][0] != EMPTY:
        return True

    # All cells have been filled without anyone winning
    if bd[0].count(EMPTY) + bd[1].count(EMPTY) + bd[2].count(EMPTY) == 0:
        return True


    # The game is still in progress
    return False





def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """


    bd = copy.deepcopy(board)

    # Determine if X won
    # 3 of X moves in a row horizontally
    for i in range (3):
        if bd[i].count(X) == 3:
             return 1
    # 3 of X moves in a row vertically
    for j in range(3):
        if bd[0][j] == bd[1][j] == bd[2][j] == X:
            return 1
    # 3 of X moves in a row diagonally
    if bd[0][0] == bd[1][1] == bd[2][2] == X:
        return 1
    elif bd[0][2] == bd[1][1] == bd[2][0] == X:
        return 1


    # Determine if O won
    # 3 of O moves in a row horizontally
    for i in range (3):
        if bd[i].count(O) == 3:
             return -1
    # 3 of O moves in a row vertically
    for j in range(3):
        if bd[0][j] == bd[1][j] == bd[2][j] == O:
            return -1
    # 3 of O moves in a row diagonally
    if bd[0][0] == bd[1][1] == bd[2][2] == O:
        return -1
    elif bd[0][2] == bd[1][1] == bd[2][0] == O:
        return -1

    # No Winner
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """



    # Count the number of X and number of O in board
    xc = board[0].count(X) + board[1].count(X) + board[2].count(X)
    oc = board[0].count(O) + board[1].count(O) + board[2].count(O)



    bdmx = copy.deepcopy(board)


    def MAX_VALUE(bdm):
        if terminal(bdm):
            return utility(bdm)


        v = -math.inf
        for ac in actions(bdm):
            v = max(v, MIN_VALUE(result(bdm, ac)))
        return v

    def MIN_VALUE(bdm):
        if terminal(bdm):
            return utility(bdm)

        v = math.inf
        for ac in actions(bdm):
            v = min(v, MAX_VALUE(result(bdm, ac)))
        return v



    # If the AI is X
    if xc == 0 and oc == 0:
        t = None
        for ac in actions(bdmx):
            mv = result(bdmx, ac)
            MV = MAX_VALUE(mv)
            P = -1
            if MV >= P:
                P = MV
                t = ac

            if MV == 1:
                return ac

        return t


    # If  the AI is O
    elif xc > oc:
        t = None
        for ac in actions(bdmx):
            mv = result(bdmx, ac)
            MV = MIN_VALUE(mv)
            P = 1
            if MV <= P:
                P = MV
                t = ac

            if MV == -1:
                return ac

        return t




    # If the AI is X
    elif xc == oc:
        t = None
        for ac in actions(bdmx):
            mv = result(bdmx, ac)
            MV = MAX_VALUE(mv)
            P = -1
            if MV >= P:
                P = MV
                t = ac

            if MV == 1:
                return ac

        return t





