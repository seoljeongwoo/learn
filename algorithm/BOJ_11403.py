import sys
input = sys.stdin.readline
n=int(input())
m=[list(map(int,input().split()))for _ in range(n)]
INF=int(1e9)
for i in range(n):
    for j in range(n):
        if m[i][j]==0: m[i][j]=INF
for k in range(n):
    for i in range(n):
        for j in range(n):
            m[i][j]=min(m[i][j],m[i][k]+m[k][j])
for i in range(n):
    for j in range(n):
        m[i][j] = 0 if m[i][j]==INF else 1
for x in m:
    print(*x)