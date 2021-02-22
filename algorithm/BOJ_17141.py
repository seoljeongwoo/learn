import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline
min_time = 2500
def bfs(pick_list):

    global min_time
    Q = deque(pick_list)
    
    visit = [[-1]*N for _ in range(N)]
    visited = M
    for x,y, in pick_list:
        visit[x][y] = 0
    _time = -1
    while Q:
        x,y = Q.popleft()

        _time = max(_time, visit[x][y])
        if _time > min_time: return

        for dx,dy in direction:
            nx,ny = x+dx, y+dy
            if nx == -1 or nx == N or ny == -1 or ny == N or visit[nx][ny] != -1 or _map[nx][ny] !=0: continue
            visit[nx][ny] = visit[x][y] + 1
            visited += 1
            Q.append((nx,ny))

    if visited != total : return
    
    min_time = min(min_time, _time)
    return

def virus_pick(index,pick_list):
    if len(pick_list) == M:
        bfs(pick_list)
        return
    if index == len(virus): return
    
    virus_pick(index+1, pick_list + [virus[index]])
    virus_pick(index+1, pick_list)
    return

N,M=map(int,input().split())
_map , virus = [] , [] 
direction = [(-1,0) , (1,0), (0,1) , (0,-1)]
total = 0
for _ in range(N):
    _map.append(list(map(int,input().split())))
    for index, data in enumerate(_map[_]):
        if data == 2: 
            virus.append((_,index))
            _map[_][index] = 0
        if data != 1:
            total += 1
virus_pick(0,[])
if min_time == 2500: print(-1)
else: print(min_time)