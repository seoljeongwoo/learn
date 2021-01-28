from collections import deque
import sys
input = sys.stdin.readline
def bfs(queue):
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if nx==-1 or nx == N or ny == -1 or ny == M: continue
            if visit[nx][ny] != -1 or farm[nx][ny] != 0: continue
            visit[nx][ny] = visit[x][y] + 1
            queue.append((nx,ny))
    ret = 0
    for i in range(N):
        for j in range(M):
            if farm[i][j] == -1: continue
            if visit[i][j] == -1: return -1
            ret = max(ret, visit[i][j])
    return ret

M,N= map(int,input().split())
farm = []
queue = deque()
dx,dy=[-1,0,1,0],[0,1,0,-1]
visit = [[-1] * M for _ in range(N)]
for _ in range(N):
    lst = list(map(int,input().split()))
    farm.append(lst)
    for idx,v in enumerate(lst):
        if v == 1:
            queue.append((_,idx))
            visit[_][idx]=0
print(bfs(queue))