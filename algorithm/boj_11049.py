import sys
input = sys.stdin.readline
n=int(input())
matrix = [list(map(int,input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]
for i in range(1,n):
    for j in range(n-i):
        dp[j][j+i] = (1<<31)
        for k in range(j,j+i):
            dp[j][j+i] = min(dp[j][j+i] , dp[j][k] + dp[k+1][j+i] + matrix[j][0]*matrix[k][1]*matrix[j+i][1])
print(dp[0][n-1])