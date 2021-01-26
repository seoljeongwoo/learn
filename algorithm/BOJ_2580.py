import sys
input = sys.stdin.readline
def row_check(used, row):
    for i in range(9):
        if board[row][i] == 0: continue
        used[board[row][i]] = False
    return used
def col_check(used, col): 
    for i in range(9):
        if board[i][col] == 0: continue
        used[board[i][col]] = False
    return used
def ran_check(used, row, col):
    sx,sy = 3*(row//3), 3*(col//3)
    for i in range(sx,sx+3):
        for j in range(sy,sy+3):
            if board[i][j] == 0 : continue
            used[board[i][j]] = False
    return used
def _back(idx):
    if idx == len(zero):
        for x in board:
            print(*x)
        sys.exit(0)
    used= [True] * 10
    used = row_check(used,zero[idx][0])
    used = col_check(used,zero[idx][1])
    used = ran_check(used,zero[idx][0], zero[idx][1])
    for i in range(1,10):
        if used[i] == True:
            board[zero[idx][0]][zero[idx][1]] = i
            _back(idx+1)
            board[zero[idx][0]][zero[idx][1]] = 0
    return 

board = [ list(map(int,input().split())) for _ in range(9)]
zero = []
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            zero.append([i,j])
_back(0)