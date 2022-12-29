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
    #count the no. of places occupied by either X or O
    xcount=0
    ocount=0
    
    #Check each row and col and decide which player should move first
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col]==X:
                xcount +=1
            if board[row][col]==O:
                ocount +=1
    if xcount > ocount:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    #create set of all possible actions

    possibleActions = set()

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == EMPTY:
                possibleActions.add((row,col))

    return possibleActions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Not a Valid Action!!")
    
    (row, col) = action
    boardcopy = copy.deepcopy(board)
    boardcopy[row][col]= player(board)
    return boardcopy

def checkRow(board, player):
    for row  in range(len(board)):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True
    return False

def checkCol(board, player):
    for col in range(len(board)):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    return False

def firstDiagonal(board, player):
    count = 0 
    for row in range(len(board)):
        for col in range(len(board[row])):
            if row ==col and board[row][col] == player:
                count +=1
    if count == 3:
        return True
    else:
        return False

def secondDiagonal(board, player):
    count = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if (len(board) - row - 1) == col and board[row][col] == player:
                count += 1
    if count == 3:
        return True
    else:
        return False

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if checkRow(board, X) or checkCol(board, X) or firstDiagonal(board, X) or secondDiagonal(board, X):
        return X
    elif checkRow(board, O) or checkCol(board, O) or firstDiagonal(board, O) or secondDiagonal(board, O):
        return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O:
        return True

    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == EMPTY:
                return False
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) ==O:
        return -1
    else:
        return 0

def max_value(board):
    v = float(-math.inf) #initial value as low as possible for finding max value
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, float(min_value(result(board, action))))
    return v

def min_value(board):
    v = float(math.inf) #initial value as high as possible 
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, float(max_value(result(board, action))))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    # x is the max player
    elif player(board) == X:
        # make a list of total plays that X has done
        totalplays = []
        # loop over possible actions
        for action in actions(board):
            # add a tuple with the min value and the action that results to that value
            totalplays.append([min_value(result(board, action)), action])
            # sort the list and reverse the value to get the action that provides max value
        return sorted(totalplays, key=lambda x: x[0], reverse = True)[0][1]

    #O is the min player
    elif player(board) == O:
        totalplays = []
        for action in actions(board):
            totalplays.append([max_value(result(board, action)), action])
        return sorted(totalplays, key=lambda x: x[0])[0][1]
    