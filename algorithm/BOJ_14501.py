import sys
input = sys.stdin.readline
N , lst, dp = int(input()), [], []
for _ in range(N):
    lst.append(list(map(int,input().split())))
    dp.append(-1)
def solve(curr):
    if curr >= N: return 0
    if dp[curr] != -1: return dp[curr]
    dp[curr] = solve(curr+1)
    if lst[curr][0] + curr <= N : dp[curr] = max(dp[curr], solve(curr+ lst[curr][0]) + lst[curr][1])
    return dp[curr]
print(solve(0))

