import sys
from itertools import permutations
from collections import deque
input =sys.stdin.readline
ret = int(1e9)
def range_check(x,y,z):
    return 0<=x<5 and 0<=y<5 and 0<=z<5

def rotate(temp, h):
    new_temp = [ [ 0 for i in range(5)] for j in range(5)]
    for i in range(5):
        for j in range(5):
            new_temp[4-j][i] = temp[h][i][j]
    for i in range(5):
        for j in range(5):
            temp[h][i][j] = new_temp[i][j]
    return temp

def bfs(temp):
    global ret
    q = deque()
    if temp[0][0][0] == 0: return
    q.append((0,0,0))
    check = [[[-1 for row in range(5)] for col in range(5)] for height in range(5)]
    check[0][0][0] = 0
    while q:
        cx, cy, cz = q.popleft()
        for dx, dy, dz in direction:
            nx,ny,nz = cx+dx, cy+dy, cz+dz
            if range_check(nx, ny, nz) == False : continue
            if check[nx][ny][nz] != -1 or temp[nx][ny][nz] == 0: continue
            check[nx][ny][nz] = check[cx][cy][cz] +1
            if check[nx][ny][nz] >= ret: return 
            q.append((nx,ny,nz))
    if check[4][4][4] == -1: return
    ret = min(ret, check[4][4][4])
    if ret == 12: print(12); exit(0)
    return

def solve(per):
    global ret
    v = [[[0 for row in range(5)] for col in range(5)] for height in range(5)]
    
    for index,height in enumerate(per):
        for row in range(5):
            for col in range(5):
                v[index][row][col] = board[height][row][col]

    for i in range(4):
        v = rotate(v,0)
        for j in range(4):
            v = rotate(v,1)
            for k in range(4):
                v = rotate(v,2)
                for l in range(4):
                    v = rotate(v,3)
                    for m in range(4):
                        v = rotate(v,4)
                        bfs(v)
    return

board = []
direction = [(0,0,1), (0,0,-1), (1,0,0), (-1,0,0) , (0,1,0) , (0,-1,0)]
for height in range(5):
    floor = []
    for row in range(5):
        floor.append(list(map(int,input().split())))
    board.append(floor)

for data in list(permutations([i for i in range(5)],5)):
    solve(data)
if ret == int(1e9): ret = -1
print(ret)