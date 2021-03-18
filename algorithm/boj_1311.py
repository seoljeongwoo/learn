import sys
input = sys.stdin.readline
def solve(curr, v):
    if v == (1<<n)-1: return 0
    if dp[curr][v] != -1: return dp[curr][v]
    dp[curr][v] = int(1e9)
    for nx in range(n):
        if v & (1<<nx): continue
        value = solve(nx, v|(1<<nx)) + m[curr][nx]
        if dp[curr][v] > value : dp[curr][v] = value
    return dp[curr][v]
n = int(input())
m = [0]*n
for i in range(n):
    m[i] = list(map(int,input().rstrip('\n').split()))
dp = [[-1]*(1<<n) for _ in range(n)]
print(solve(0,1))   