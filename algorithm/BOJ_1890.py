import sys
input = sys.stdin.readline
N = int(input())
J , DP = [list(map(int,input().split())) for _ in range(N)] , [ [0]*N for _ in range(N)]
DP[0][0] = 1
for i in range(N):
    for j in range(N):
        if DP[i][j] != 0 and J[i][j] != 0:
            nx,ny = i+J[i][j] , j+ J[i][j]
            if 0<=nx<N: DP[nx][j] += DP[i][j]
            if 0<=ny<N: DP[i][ny] += DP[i][j]
print(DP[N-1][N-1])