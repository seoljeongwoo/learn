import sys
input = sys.stdin.readline
def solve(c,v):
    if v == (1<<n)-1 : return w[c][0] if w[c][0] else int(1e9)
    if dp[c][v] != -1: return dp[c][v]
    ret = int(1e9)
    for x in range(n):
        if v&(1<<x) or w[c][x] ==0: continue
        ret=  min(ret, solve(x,v|(1<<x)) + w[c][x])
    dp[c][v] = ret
    return dp[c][v]
n = int(input())
w = [list(map(int,input().split())) for _ in range(n)]
dp = [[-1]*(1<<n) for _ in range(n)]
print(solve(0,1))