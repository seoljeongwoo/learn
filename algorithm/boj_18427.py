import sys
sys.setrecursionlimit(50505)
input = sys.stdin.readline

def solve(c, s):
    if s == 0: return 1
    if c == n: return 0
    if dp[c][s] != -1: return dp[c][s]
    dp[c][s] = solve(c+1,s)%mod
    for data in lst[c]:
        if s-data >=0 : 
            dp[c][s] += solve(c+1,s-data)
            dp[c][s] %= mod
    return dp[c][s]
n,m,h= map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(n)]
dp = [[-1]*(h+1) for _ in range(n)]
mod = 10007
print(solve(0,h))