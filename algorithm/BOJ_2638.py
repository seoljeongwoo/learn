import sys
from collections import deque
input = sys.stdin.readline
n,m=map(int,input().split())
b = [[0]*(m+2) for _ in range(n+2)]
lst = [list(map(int,input().split())) for _ in range(n)]
for i in range(n):
    for j in range(m):
        b[i+1][j+1]=lst[i][j]

v = [[0]*(m+2) for _ in range(n+2)]
direction = [(-1,0),(1,0),(0,1),(0,-1)]
w,nw=[],[]
q=deque()
q.append((0,0))
v[0][0]= -1
melt=[]
t =0
while True:
    #치즈내부로 물이 침투할수있으면 침투
    while q:
        cx,cy=q.popleft()
        w.append((cx,cy))
        for dx, dy in direction:
            nx,ny=cx+dx,cy+dy
            if nx==-1 or nx==n+2 or ny==-1 or ny==m+2 or b[nx][ny]==1 or v[nx][ny]!=0: continue
            v[nx][ny]=-1;q.append((nx,ny))
            
    #치즈녹이기 
    while w:
        x,y=w.pop()
        for dx,dy in direction:
            nx,ny=x+dx,y+dy
            if nx==-1 or nx==n+2 or ny==-1 or ny==m+2 or b[nx][ny]==0 : continue
            v[nx][ny]+=1
            if v[nx][ny]==2:
                b[nx][ny]=0;v[nx][ny]=-1;q.append((nx,ny));melt.append((nx,ny))
    if len(melt)==0: break
    melt,t=[],t+1
print(t)
