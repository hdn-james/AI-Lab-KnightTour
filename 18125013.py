import argparse
import random
from timeit import default_timer as timer
import time
import backtracking as backtrack
import warnsdorffs as wd

def parameterCheck(px,py,m):
    print("px = {}".format(px))
    print("py = {}".format(py))
    print("m = {}".format(m))
    print("")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-px', '--px', help = 'Start at x')
    parser.add_argument('-py', '--py', help = 'Start at y')
    parser.add_argument('-m', '--m', help = 'Size of the board')
    args = parser.parse_args()

    px = int(args.px)
    py = int(args.py)
    m = int(args.m)

    parameterCheck(px,py,m) 
    # list = [5,8,15]

    # for i in list:
    #     print("Board {} x {}".format(i,i))
    #     start = timer()
    #     backtrack.solutionKnightTour(px,py,i)
    #     end = timer()
    #     print("Took " + str(end-start) + " second")
    #     print("")  

    random.seed(time.time())
    while not wd.solution(m):
        continue

if __name__ == "__main__":
    main()
