import sys
input = sys.stdin.readline
N,M,K= map(int,input().split())
a = [list(map(int,input().split())) for _ in range(N)]
dx,dy=[1,0,-1,0],[0,1,0,-1]
for i in range(min(N,M)//2):
    x,y,lst,d = i,i,[],0
    lst.append((x,y,a[x][y]))
    while True:
        x,y=x+dx[d],y+dy[d]
        if x==(-1+i) or x == (N-i) or y == (-1+i) or y == (M-i):
            x,y=x-dx[d], y-dy[d]
            d+=1
            x,y=x+dx[d],y+dy[d]
        if x==i and y==i:
            break
        lst.append((x,y,a[x][y]))
    for j in range(len(lst)):
        nx,ny,v = lst[j]
        a[nx][ny] = lst[ (j-K) % len(lst)][2]
for x in a:
    print(*x)

