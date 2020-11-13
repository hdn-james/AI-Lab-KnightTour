def isSafe(x, y, board, m):
    return bool(x >= 0 and y >= 0 and x < m and y < m and board[x][y] == -1)

def outputSolution(m, board):
    for i in range(m):
        for j in range(m):
            print(str(board[i][j]), end='\t')
        print("")

def solutionKnightTour(px,py,m):
    board = [ [ -1 for i in range(m) ] for i in range(m) ]
        
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]
    board[px][py] = 0
    pos = 1
    if(not solutionUtil(m, board, px, py, move_x, move_y, pos)):
        print("Solution does not exist")
    else:
        outputSolution(m, board)

def solutionUtil(m, board, curr_x, curr_y, move_x, move_y, pos):
    if(pos == m**2):
        return True
    for i in range(8):
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]
        if(isSafe(new_x, new_y, board, m)):
            board[new_x][new_y] = pos
            if(solutionUtil(m, board, new_x, new_y, move_x, move_y, pos+1)):
                return True
            board[new_x][new_y] = -1
    return False