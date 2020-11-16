import os
from multiprocessing import Process
import multiprocessing
from timeit import default_timer as timer

def thread1():
    for i in range(8):
        path = "python3 18125013_backtracking.py -px 0 "+ " -py " + str(i) + " -m 8"
        os.system(path)
def thread2():
    for i in range(8):
        path = "python3 18125013_backtracking.py -px 1 "+ " -py " + str(i) + " -m 8"
        os.system(path)
def thread3():
    for i in range(8):
        path = "python3 18125013_backtracking.py -px 2 "+ " -py " + str(i) + " -m 8"
        os.system(path)
def thread4():
    for i in range(8):
        path = "python3 18125013_backtracking.py -px 3 "+ " -py " + str(i) + " -m 8"
        os.system(path)
def thread5():
    for i in range(8):
        path = "python3 18125013_backtracking.py -px 4 "+ " -py " + str(i) + " -m 8"
        os.system(path)
def thread6():
    for i in range(8):
        path = "python3 18125013_backtracking.py -px 5 "+ " -py " + str(i) + " -m 8"
        os.system(path)
def thread7():
    for i in range(8):
        path = "python3 18125013_backtracking.py -px 6 "+ " -py " + str(i) + " -m 8"
        os.system(path)
def thread8():
    for i in range(8):
        path = "python3 18125013_backtracking.py -px 7 "+ " -py " + str(i) + " -m 8"
        os.system(path)


def main():
    print("number of cpu : {}".format(multiprocessing.cpu_count()))
    procs = []
    name = [thread1, thread2, thread3, thread4, thread5, thread6, thread7, thread8] 
    for i in name:
        proc = Process(target=i)
        procs.append(proc)
        proc.start()
    for proc in procs:
        proc.join()

if __name__ == "__main__":
    start = timer()
    os.system("mkdir ../OUTPUT")
    # Run Backtracking with board size 8x8
    os.system("mkdir ../OUTPUT/Backtracking_8x8") # Create OUTPUT folder

    main()

    end = timer()
    print("Finished in {} second".format(str(end-start)))
