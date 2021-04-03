import numpy as np
mat = []
for _ in range(9):
    li = list(map(int, input().split()))
    mat.append(li)

def possible(x,y,n):
    for i in range(0,9):
        if mat[x][i] == n:
            return False
    for i in range(0,9):
        if mat[i][y] == n:
            return False
    x_sq = (x//3)*3
    y_sq = (y//3)*3
    for i in range(3):
        for j in range(3):
            if mat[x_sq+i][y_sq+j] == n:
                return False
    return True

def result():
    for i in range(9):
        for j in range(9):
            if mat[i][j] == 0:
                for n in range(1, 10):
                    if possible(i, j, n):
                        mat[i][j] = n
                        result()
                        mat[i][j] = 0
                return
    print(np.matrix(mat))

result()
