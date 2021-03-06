import sys
input = sys.stdin.readline

n,k=map(int,input().split())
dp = [[0]*(k+1) for _ in range(2)]
for i in range(n):
    a = int(input())
    for j in range(k+1):
        if j<a: dp[i%2][j] = dp[(i+1)%2][j]
        else: dp[i%2][j] = max(dp[(i+1)%2][j], dp[(i+1)%2][j-a] + 1)
print(dp[n%2][k])