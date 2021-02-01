N = int(input())
dp = [-1]*(N+1)
dp[1] = 0
for i in range(1,N):
    if dp[i] == -1: continue
    if i*3 <=N and (dp[i*3]==-1 or dp[i*3]>dp[i] + 1): dp[i*3] = dp[i]+1
    if i*2<=N and (dp[i*2]==-1 or dp[i*2] > dp[i] + 1): dp[i*2] = dp[i]+1
    if i+1<=N and (dp[i+1]==-1 or dp[i+1] > dp[i]+1):dp[i+1] = dp[i]+1
print(dp[N])
