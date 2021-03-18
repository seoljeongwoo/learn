import sys
input = sys.stdin.readline
n,m=int(input()) , int(input())
dist = [[(1<<31)]*(n+1) for _ in range(n+1)]
path = [[0]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        path[i][j] = []

for i in range(1,n+1): dist[i][i] = 0
for _ in range(m):
    u,v,w= map(int,input().split())
    dist[u][v] = min(dist[u][v] , w)

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                path[i][j] = path[i][k] + [k] + path[k][j]
                dist[i][j] = dist[i][k] + dist[k][j]

for i in range(1,n+1):
    for j in range(1,n+1):
        if dist[i][j] == (1<<31): dist[i][j] = 0
        print(dist[i][j] , end= " ")
    print()
    
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j : print(0);continue
        print(len(path[i][j]) + 2, end =" ")
        print(i,end =" ")
        for x in path[i][j]: print(x, end = " ")
        print(j)