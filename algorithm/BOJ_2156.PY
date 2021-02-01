import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
def solve(c,j):
    if c>N: return 0
    if dp[c][j] != -1: return dp[c][j]
    ret = 0
    if j<=1: ret = max(ret, solve(c+1,j+1) + g[c])
    ret = max(ret, solve(c+1,0))
    dp[c][j] = ret
    return dp[c][j]
N , g = int(input()) , [0]
for _ in range(N):
    g.append(int(input()))
dp = [[-1]*3 for _ in range(N+1)]
print(solve(0,0))