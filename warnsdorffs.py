import random

cx = [1,1,2,2,-1,-1,-2,-2]
cy = [2,-2,1,-1,2,-2,1,-1]

def limits(x, y, m):
    return bool((x >= 0 and y >= 0) and (x < m and y < m))

def isEmpty(a, x, y, m):
    return bool(limits(x, y, m)) and (a[y*m+x] < 0)

def getDegree(a, x, y, m):
    cnt = 0
    for i in range (m):
        if isEmpty(a,(x + cx[i]), (y + cy[i]), m):
            cnt += 1
    return cnt

def nextMove(a, x, y, m):
    min_deg_idx = -1
    c = 0 
    min_deg = (m+1) 
    nx = 0
    ny = 0
    start = random.randint(0,m)
    for count in range(m):
        i = (start + count) % m
        nx = x + cx[i]
        ny = y + cy[i]
        c = getDegree(a, nx, ny, m)
        if isEmpty(a, nx, ny, m) and c < min_deg:
            min_deg_idx = i
            min_deg = c
    if min_deg_idx == -1:
        return False
    nx = x + cx[min_deg_idx]
    ny = y + cy[min_deg_idx] 
    a[ny*m + nx] = a[(y)*m + (x)]+1
    x = nx
    y = ny
    return True

def printSolution(a, m):
    for i in range(m):
        for j in range(m):
            print(str(a[j*m+i]), end='\t') 
        print("")

def neighbor(x, y, xx, yy, m):
    for i in range (m):
        if ((x+cx[i]) == xx) and ((y + cy[i]) == yy):
            return True
    return False

def solution(m):
    a = [-1 for i in range(m*m)]
    sx = random.randint(0,m)
    sy = random.randint(0,m)
    x = sx
    y = sy
    a[y*m+x] = 1
    for i in range (m*m-1):
        if nextMove(a, x, y, m) == 0:
            return False
    if (not neighbor(x,y,sx,sy,m)):
        return False
    printSolution(a,m)
    return True
