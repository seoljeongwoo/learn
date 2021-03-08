import sys
from collections import deque
input = sys.stdin.readline
def check(x,y):
    return 0<=x<n and 0<=y<n
n,m=map(int,input().split())
edge =[[] for _ in range(10101)]
for _ in range(m):
    x,y,a,b=map(int,input().split())
    x-=1;y-=1;a-=1;b-=1
    edge[x*100+y].append((a,b))

direction=[(-1,0),(1,0),(0,1),(0,-1)]
light,move,visit=[[False]*n for _ in range(n)],[[False]*n for _ in range(n)],[[False]*n for _ in range(n)]
light[0][0]=move[0][0]=visit[0][0]=True
q=deque()
q.append((0,0))
while q:
    x,y=q.popleft()
    for dx,dy in direction:
        nx,ny=x+dx,y+dy
        if check(nx,ny):
            move[nx][ny]=True

    for nx,ny in edge[x*100+y]:
        if light[nx][ny]==False: 
            light[nx][ny]=True
            if move[nx][ny]: q.append((nx,ny))

    for dx,dy in direction:
        nx,ny=x+dx,y+dy
        if check(nx,ny) and light[nx][ny] and not visit[nx][ny]:
            visit[nx][ny]=True
            q.append((nx,ny))
cnt=0
for i in range(n):
    for j in range(n):
        if light[i][j]: cnt+=1

print(cnt)