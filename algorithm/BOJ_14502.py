import sys
import copy
from collections import deque
input = sys.stdin.readline

result = 0
def bfs(safe_cnt):
    global result
    new_lst = copy.deepcopy(lst)
    q = deque(virus)
    while q:
        x,y = q.popleft()
        for dx,dy in direction:
            nx,ny = x+dx,y+dy
            if nx == -1 or nx == N or ny == -1 or ny == M: continue
            if new_lst[nx][ny] != 0: continue
            new_lst[nx][ny] = 2
            q.append((nx,ny))
            safe_cnt -= 1
   
    result = max(result, safe_cnt)
    return

def go(index ,pick , safe_cnt):
    if len(pick) == 3:
        bfs(safe_cnt)
        return

    if index == len(wall): return

    x,y = wall[index]

    lst[x][y] = 1
    go(index+1,pick + [wall[index]], safe_cnt -1)

    lst[x][y] = 0
    go(index+1,pick , safe_cnt)

    return

N,M = map(int,input().split())
lst = [ list(map(int,input().split())) for _ in range(N)]
wall,virus = [], []
direction = [(-1,0),(1,0),(0,1),(0,-1)]
for i in range(N):
    for j in range(M):
        if lst[i][j] == 0: wall.append((i,j))
        elif lst[i][j] == 2: virus.append((i,j))
        
safe = len(wall)
go(0,[],safe)

print(result)