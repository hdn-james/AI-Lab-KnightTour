import argparse
import signal
import sys
from timeit import default_timer as timer

sys.setrecursionlimit(10000)
class Backtracking:
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]
    def __init__(self, px, py, m):
        self.size = m
        self.counter = 0
        self.px = px
        self.py = py
        self.board = [ [ -1 for _ in range(m) ] for _ in range(m) ]

    def isSafe(self, x, y):
        return bool(x >= 0 and y >= 0 and x < self.size and y < self.size and self.board[x][y] == -1)

    def outputSolution(self):
        for i in range(self.size):
            for j in range(self.size):
                print(str(self.board[i][j] + 1))
            print("")

    def solutionKnightTour(self):
        self.board[self.px][self.py] = 0
        pos = 1
        if(not self.solutionUtil(self.px, self.py, Backtracking.move_x, Backtracking.move_y, pos)):
            return False
        else:
            return True

    def solutionUtil(self, curr_x, curr_y, move_x, move_y, pos):          
        if(pos == self.size*self.size):
            return True
        for i in range(8):
            new_x = curr_x + Backtracking.move_x[i]
            new_y = curr_y + Backtracking.move_y[i]
            if self.isSafe(new_x, new_y):
                self.counter += 1
                self.board[new_x][new_y] = pos
                if self.solutionUtil(new_x, new_y, Backtracking.move_x, Backtracking.move_y, pos+1):
                    return True
                self.board[new_x][new_y] = -1
        return False

def handler(signum, frame):
    raise Exception("end of time")
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-px', '--px', help = 'Start at x')
    parser.add_argument('-py', '--py', help = 'Start at y')
    parser.add_argument('-m', '--m', help = 'Size of the board')
    args = parser.parse_args()
    px = int(args.px)
    py = int(args.py)
    m = int(args.m)
    path_to_file = "OUTPUT/Backtracking_" + str(m) + "x" + str(m) + "/18125013_backtracking_" + str(m) + "x" + str(m) + "_" + str(px) + "_" + str(py) + ".txt"

    file = open(path_to_file,"w")
    file.write("{} {} {}\n".format(px, py, m))

    bt = Backtracking(px,py,m)
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(300)
    start_time = timer()
    try:
        sol = bt.solutionKnightTour()
        end_time = timer()
        file.write("{}\n".format(bt.counter))
        file.write("{}\n".format((end_time-start_time)*1000))
        if sol:
            for i in range(bt.size):
                for j in range(bt.size):
                    file.write("{} ".format(bt.board[i][j] + 1))
                file.write("\n")
        else:
            file.write("Solution does not exist")
        file.write("\n")
    except Exception:
        file.write("{}\n".format(bt.counter))
        file.write("{}\n".format(1000*(timer()-start_time)))
        file.write("Time limit exceeded")
    signal.alarm(0)
    file.close()