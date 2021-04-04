import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline
def range_check(x,y):
    return 0<=x<n and 0<=y<n
def bfs(target):
    v = [[-1]*n for _ in range(n)]
    q = deque()
    paint = len(target)
    ret = 0
    for x,y in target:
        q.append((x,y)); v[x][y] = 0
    while q:
        cx,cy = q.popleft()
        if state[cx][cy] != 2: ret = max(v[cx][cy] , ret)
        for dx, dy in direction:
            nx,ny =cx+dx,cy+dy
            if not range_check(nx,ny) : continue
            if v[nx][ny] != -1 or state[nx][ny] ==1: continue
            v[nx][ny] = v[cx][cy] + 1
            q.append((nx,ny))
            paint += 1
 
    if paint == zero: return ret
    return int(1e9)
    

n,m = map(int,input().split())
state = [list(map(int,input().split())) for _ in range(n)]
virus = []
direction = [(-1,0),(0,1),(0,-1),(1,0)]
zero = 0
for i, row in enumerate(state):
    for j,data in enumerate(row):
        if data == 2: virus.append((i,j)); zero+=1
        if data == 0: zero+=1

ret = int(1e9)
for data in list(combinations(virus,m)):
    ret = min(ret, bfs(data))
if ret == int(1e9): ret = -1
print(ret)