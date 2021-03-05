import sys
from collections import deque
input = sys.stdin.readline
def bfs01():
    visit = [[-1] * M for _ in range(N)]
    direction = [(-1,0),(1,0),(0,1),(0,-1)]
    q = deque()
    q.append((0,0,0))
    while q:
        x,y,c=q.popleft()
        if visit[x][y] != -1: continue
        visit[x][y] = c
        for dx,dy in direction:
            nx,ny = x+ dx, y+ dy
            if nx==-1 or nx==N or ny==-1 or ny==M or visit[nx][ny]!=-1: continue
            if board[nx][ny] =='1': q.append((nx,ny,c+1))
            else: q.appendleft((nx,ny,c))
    return visit[N-1][M-1]
    
M,N=map(int,input().split())
board = [list(input().rstrip('\n')) for _ in range(N)]
print(bfs01())