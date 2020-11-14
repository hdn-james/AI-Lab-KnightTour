import argparse
from timeit import default_timer as timer

class Warnsdorffs:
    _knight_jumps = ((-2, 1), (-2, -1), 
                    (2, 1), (2, -1),
                    (1, -2), (-1, -2),
                    (1, 2), (-1, 2))
    def __init__(self, n, m, i, j):
        initial = i * m + j
        self.positions = [initial]
        self.n = n
        self.m = m 
        self.visited = [False for _ in range(n * m)]
        self.visited[initial] = True
        
    def check_on_board(self, i, j):
        return i >= 0 and i < self.n and j >= 0 and j < self.m
    
    def calculate(self, p):
        count = 0
        i, j = p / self.m, p % self.m
        for jump in Warnsdorffs._knight_jumps:
            if self.check_on_board(i + jump[0], j + jump[1]) and self.visited[(i + jump[0]) * self.m + j + jump[1]] == False:
                count += 1
        return count
    
    def start(self):
        count = 1
        while self.step() != None:
            count += 1
        return self.positions, count, count == self.n * self.m
    
    def step(self):
        i = self.positions[-1] / self.m
        j = self.positions[-1] % self.m
        pos = []
        for jump in Warnsdorffs._knight_jumps:
            p = (i + jump[0]) * self.m + j + jump[1]
            if self.check_on_board(i + jump[0], j + jump[1]) and self.visited[p] == False:                
                pos.append((self.calculate(p), p))
        if len(pos) != 0:
            pos = sorted(pos,key = lambda v: v[0]) 
            self.positions.append(pos[0][1])
            self.visited[pos[0][1]] = True
            return pos[0][1]
        else:
            return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-px', '--px', help = 'Start at x')
    parser.add_argument('-py', '--py', help = 'Start at y')
    parser.add_argument('-m', '--m', help = 'Size of the board')
    args = parser.parse_args()
    px = int(args.px)
    py = int(args.py)
    m = int(args.m)

    path_to_file = "../OUTPUT/18125013_heuristic_" + str(m) + "x" + str(m) + "_" + str(px) + "_" + str(py) + ".txt"

    file = open(path_to_file,"a")
    file.write("{} {} {}\n".format(px,py,m))
    kt = Warnsdorffs(m,m,px,py) 
    start_time = timer()
    sol = kt.start()
    end_time = timer()
    board = [ [ -1 for i in range(m) ] for i in range(m) ]
    t = 0
    for pos in kt.positions:
        row = pos / m
        col = pos % m
        board[row][col] = t
        t += 1


    file.write("{}\n".format(sol[1]))
    file.write("{} millisecond\n".format((end_time-start_time)*1000))
    for i in range(m):
        for j in range(m):
            file.write("{} ".format(str(board[i][j])))
        file.write("\n")
    file.write('\n')
    file.close()
