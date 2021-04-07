import sys
from collections import deque
input = sys.stdin.readline
def range_check(x,y):
    return 0<=x<n and 0<=y<m

def attack(x,y,d):
    if state[x][y] == False: return 0
    q = deque()
    q.append((x,y))
    state[x][y] = False
    ret = 1
    while q:
        cx,cy = q.popleft()
        power = domino[cx][cy]
        for i in range(power-1):
            nx,ny = cx+direction[d][0]*(i+1), cy+direction[d][1]*(i+1)
            if range_check(nx,ny) == False: continue
            if state[nx][ny] == False: continue
            ret += 1
            state[nx][ny] = False
            q.append((nx,ny))
    return ret
def defence(x,y):
    state[x][y] = True
    return
n,m,r = map(int,input().split())
domino = [list(map(int,input().split())) for _ in range(n)]
state = [ [True] * m for _ in range(n) ]
a = {}
a['E'] = 0; a['W'] = 1; a['N'] = 2; a['S'] = 3
direction = [(0,1) , (0,-1) , (-1,0) , (1,0)]
attack_point = 0
for _ in range(r):
    row, col, d = input().split()
    attack_point += attack(int(row)-1, int(col)-1, a[d])

    row,col = map(int,input().split())
    defence(row-1,col-1)
print(attack_point)
for i in range(n):
    for j in range(m):
        if state[i][j] == True: print('S', end=" ")
        else : print('F', end=" ")
    print()