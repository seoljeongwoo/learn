N = int(input())
dp = [[0]*N for _ in range(10)]
for i in range(1,10):
    dp[i][0] = 1
for i in range(1,N):
    for j in range(10):
        dp[j][i-1]%=1000000000
        if j==0:
            dp[j+1][i] += dp[j][i-1]
        elif j==9:
            dp[j-1][i] += dp[j][i-1]
        else:
            dp[j+1][i] += dp[j][i-1]
            dp[j-1][i] += dp[j][i-1]
result = 0
for _ in range(10):
    result += dp[_][N-1]%1000000000
print(result%1000000000)