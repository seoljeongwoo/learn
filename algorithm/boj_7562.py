import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
direction = [(-1,-2),(-2,-1),(-2,1),(-1,2),(1,-2),(2,-1),(2,1),(1,2)]
def range_check(x,y):
    return 0<=x<l and 0<=y<l
for _ in range(t):
    l = int(input())
    sx,sy = map(int,input().split())
    ex,ey = map(int,input().split())
    q = deque()
    q.append((sx,sy))
    v = [[-1] * l for _ in range(l)]
    v[sx][sy] = 0
    while q:
        cx,cy = q.popleft()
        if v[ex][ey] != -1: break
        for dx, dy in direction:
            nx,ny = cx+dx, cy+dy
            if range_check(nx,ny) == False: continue
            if v[nx][ny] != -1: continue
            v[nx][ny] = v[cx][cy] +1
            q.append((nx,ny))
    print(v[ex][ey])