"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None
SIZE = 3

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
    xcounter = sum(row.count(X) for row in board)
    ocounter = sum(row.count(O) for row in board)
    if xcounter == ocounter:
        return X
    else : #xcounter > ocounter
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actionset = set()
    SIZE = 3
    for i in range(SIZE):
        for j in range(SIZE):
            if board[i][j] == EMPTY:
                actionset.add((i,j))
    
    return actionset
            

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    ac = actions(board)
    if action not in ac:
        raise Exception
    
    board2 = copy.deepcopy(board)
    pl = player(board)
    i = action[0]
    j = action[1]
    if pl == X :
        board2[i][j] = "X"
    else :
        board2[i][j] = "O"

    return board2

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if specificwinner(board , X) == X:
        return X
    return specificwinner(board , O)

def specificwinner(board , symbol):
    countcols = 0
    countrows = 0 
    for j in range(SIZE):
        for i in range(SIZE):
            if board[i][j] == symbol :
                countcols += 1
            if board[j][i] == symbol:
                countrows += 1
        if countcols == SIZE or countrows == SIZE:
            return symbol
        countcols = 0
        countrows = 0
    #diagonally
    if board[1][1] == symbol and ((board[0][0] == symbol and board[2][2] == symbol) or (board[0][2] == symbol and board[2][0] == symbol)):
        return symbol
    return None

def is_empty(board):
    """
    Check if there is an empty space on the board.
    """
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return True
    return False

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    w = winner(board)
    if  w != None or is_empty(board) == False:
        return True
    return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w = winner(board)
    if w == X:
        return 1
    elif w == O:
        return -1
    else : return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    if player(board) == X: 
        best_val = -math.inf
        for action in actions(board):
            val =  minvalue(result(board, action))
            if val > best_val:
                best_val = val
                optimal_act = action
        return optimal_act
    else : #player(board) == O
        best_val = math.inf
        for action in actions(board):
            val =  maxvalue(result(board, action))
            if val < best_val:
                best_val = val
                optimal_act = action
        return optimal_act

     
def maxvalue(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v,minvalue(result(board, action))) 
  
    return v

def minvalue(board):
    if terminal(board):
        return utility(board)

    v = math.inf
    for action in actions(board):
        v =  min(v,maxvalue(result(board, action)))

    return v


