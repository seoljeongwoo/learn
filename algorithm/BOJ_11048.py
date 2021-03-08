import sys
input = sys.stdin.readline
n,m=map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(n)]
dp=[[0]*(m+1) for _ in range(n+1)]
for i in range(n):
    for j in range(m):
        dp[i][j] += lst[i][j]
        dp[i+1][j] = max(dp[i+1][j],dp[i][j])
        dp[i][j+1] = max(dp[i][j+1],dp[i][j])
        dp[i+1][j+1]=max(dp[i+1][j+1],dp[i][j])
print(dp[n-1][m-1])