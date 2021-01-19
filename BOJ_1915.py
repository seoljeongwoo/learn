import sys
input = sys.stdin.readline
n,m = map(int,input().split())
rec = [list(input()) for _ in range(n)]
dp = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        dp[i][j] = int(rec[i][j])

for i in range(1,n):
    for j in range(1,m):
        if dp[i][j] == 0 : continue
        minvalue = min(dp[i-1][j] , min(dp[i][j-1] , dp[i-1][j-1]))
        dp[i][j] = minvalue + 1
max_length = 0
for data in dp:
    max_length = max(max_length , max(data))
print(max_length * max_length)

