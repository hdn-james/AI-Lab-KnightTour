import os
from multiprocessing import Process
import multiprocessing
from timeit import default_timer as timer

def RUN():
    os.system("mkdir ../OUTPUT")
    os.system("mkdir ../OUTPUT/Heuristic_5x5") # Create OUTPUT folder
    os.system("mkdir ../OUTPUT/Heuristic_8x8") # Create OUTPUT folder
    os.system("mkdir ../OUTPUT/Heuristic_15x15") # Create OUTPUT folder
    os.system("mkdir ../OUTPUT/Heuristic_25x25") # Create OUTPUT folder
    os.system("mkdir ../OUTPUT/Heuristic_40x40") # Create OUTPUT folder
    os.system("mkdir ../OUTPUT/Backtracking_5x5") # Create OUTPUT folder
    os.system("mkdir ../OUTPUT/Backtracking_15x15") # Create OUTPUT folder
    os.system("mkdir ../OUTPUT/Backtracking_25x25") # Create OUTPUT folder
    os.system("mkdir ../OUTPUT/Backtracking_40x40") # Create OUTPUT folder
    # Run Warnsdorffs Heuristic with board size 5x5
    os.system("python3 18125013_warnsdorffs.py -px 1 -py 2 -m 5")
    os.system("python3 18125013_warnsdorffs.py -px 4 -py 3 -m 5")
    os.system("python3 18125013_warnsdorffs.py -px 3 -py 1 -m 5")
    os.system("python3 18125013_warnsdorffs.py -px 0 -py 0 -m 5")
    os.system("python3 18125013_warnsdorffs.py -px 2 -py 4 -m 5")
    # Run Warnsdorffs Heuristic with board size 8x8
    os.system("python3 18125013_warnsdorffs.py -px 0 -py 0 -m 8")
    os.system("python3 18125013_warnsdorffs.py -px 3 -py 5 -m 8")
    os.system("python3 18125013_warnsdorffs.py -px 5 -py 1 -m 8")
    os.system("python3 18125013_warnsdorffs.py -px 7 -py 3 -m 8")
    os.system("python3 18125013_warnsdorffs.py -px 1 -py 7 -m 8")
    # Run Warnsdorffs Heuristic with board size 15x15
    os.system("python3 18125013_warnsdorffs.py -px 0 -py 0 -m 15")
    os.system("python3 18125013_warnsdorffs.py -px 3 -py 12 -m 15")
    os.system("python3 18125013_warnsdorffs.py -px 6 -py 9 -m 15")
    os.system("python3 18125013_warnsdorffs.py -px 9 -py 4 -m 15")
    os.system("python3 18125013_warnsdorffs.py -px 12 -py 7 -m 15")
    # Run Warnsdorffs Heuristic with board size 25x25
    os.system("python3 18125013_warnsdorffs.py -px 0 -py 0 -m 25")
    os.system("python3 18125013_warnsdorffs.py -px 23 -py 12 -m 25")
    os.system("python3 18125013_warnsdorffs.py -px 14 -py 18 -m 25")
    os.system("python3 18125013_warnsdorffs.py -px 8 -py 17 -m 25")
    os.system("python3 18125013_warnsdorffs.py -px 2 -py 10 -m 25")
    # Run Warnsdorffs Heuristic with board size 40x40
    os.system("python3 18125013_warnsdorffs.py -px 0 -py 0 -m 40")
    os.system("python3 18125013_warnsdorffs.py -px 10 -py 30 -m 40")
    os.system("python3 18125013_warnsdorffs.py -px 15 -py 24 -m 40")
    os.system("python3 18125013_warnsdorffs.py -px 9 -py 36 -m 40")
    os.system("python3 18125013_warnsdorffs.py -px 28 -py 7 -m 40")
    # Run Backtracking with board size 5x5
    os.system("python3 18125013_backtracking.py -px 1 -py 2 -m 5")
    os.system("python3 18125013_backtracking.py -px 4 -py 3 -m 5")
    os.system("python3 18125013_backtracking.py -px 3 -py 1 -m 5")
    os.system("python3 18125013_backtracking.py -px 0 -py 0 -m 5")
    os.system("python3 18125013_backtracking.py -px 2 -py 4 -m 5")

run = [
    "python3 18125013_backtracking.py -px 0 -py 0 -m 15",
    "python3 18125013_backtracking.py -px 3 -py 12 -m 15",
    "python3 18125013_backtracking.py -px 6 -py 9 -m 15",
    "python3 18125013_backtracking.py -px 9 -py 4 -m 15",
    "python3 18125013_backtracking.py -px 12 -py 7 -m 15",
    "python3 18125013_backtracking.py -px 0 -py 0 -m 25",
    "python3 18125013_backtracking.py -px 23 -py 12 -m 25",
    "python3 18125013_backtracking.py -px 14 -py 18 -m 25"
]
run2 = [
    "python3 18125013_backtracking.py -px 8 -py 17 -m 25",
    "python3 18125013_backtracking.py -px 2 -py 10 -m 25",
    "python3 18125013_backtracking.py -px 0 -py 0 -m 40",
    "python3 18125013_backtracking.py -px 10 -py 30 -m 40",
    "python3 18125013_backtracking.py -px 15 -py 24 -m 40",
    "python3 18125013_backtracking.py -px 9 -py 36 -m 40",
    "python3 18125013_backtracking.py -px 28 -py 7 -m 40",
]

def t1():
    os.system(run[0])
    os.system(run2[0])
def t2():
    os.system(run[1])
    os.system(run2[1])
def t3():
    os.system(run[2])
    os.system(run2[2])
def t4():
    os.system(run[3])
    os.system(run2[3])
def t5():
    os.system(run[4])
    os.system(run2[4])
def t6():
    os.system(run[5])
    os.system(run2[5])
def t7():
    os.system(run[6])
    os.system(run2[6])
def t8():
    os.system(run[7])


def main():
    print("number of cpu : {}".format(multiprocessing.cpu_count()))
    RUN()
    procs = []
    name = [t1, t2, t3, t4, t5, t6, t7, t8] 
    for i in name:
        proc = Process(target=i)
        procs.append(proc)
        proc.start()
    for proc in procs:
        proc.join()

if __name__ == "__main__":
    start = timer()

    main()

    end = timer()
    print("Finished in {} second".format(str(end-start)))