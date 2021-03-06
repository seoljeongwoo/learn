import sys
from collections import deque
input = sys.stdin.readline

r,c= map(int,input().split())
swan,m_swan,nm_swan,w,nw=[],deque(),deque(),deque(),deque()
lake=[list(input().rstrip('\n')) for _ in range(r)]
for i in range(r):
    for j in range(c):
        if lake[i][j] == 'L':
            swan.append((i,j))
            lake[i][j] = '.'
            w.append((i,j))
        elif lake[i][j] == '.':
            w.append((i,j))

day =0
direction = [(-1,0),(1,0),(0,1),(0,-1)]
sx,sy=swan[0]
ex,ey=swan[1]
v = [[False]*c for _ in range(r)]
v[sx][sy] = True
m_swan.append((sx,sy))
while True:
    while m_swan:
        cx,cy=m_swan.popleft()
        if cx==ex and cy==ey:
            print(day)
            exit(0)
        for dx,dy in direction:
            nx,ny=cx+dx,cy+dy
            if nx==-1 or nx==r or ny==-1 or ny==c or v[nx][ny]: continue
            if lake[nx][ny] == '.':
                v[nx][ny] = True; m_swan.append((nx,ny))
            elif lake[nx][ny] == 'X':
                v[nx][ny] = True; nm_swan.append((nx,ny))

    while w:
        cx,cy=w.popleft()
        for dx, dy in direction:
            nx,ny=cx+dx,cy+dy
            if nx==-1 or nx==r or ny==-1 or ny==c: continue
            if lake[nx][ny] == 'X':
                lake[nx][ny] = '.'
                nw.append((nx,ny))
    m_swan ,nm_swan = nm_swan, deque()
    w,nw=nw,deque()
    day+=1
