import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline
def solve(curr, prev, first):
    if curr == n-1:
        ret = int(1e9)
        for i in range(3):
            if prev ==i or first == i: continue
            ret = min(ret, m[curr][i])
        return ret
    
    if dp[curr][prev] != -1: return dp[curr][prev]
    dp[curr][prev] = int(1e9)
    
    for i in range(3):
        if prev == i: continue
        dp[curr][prev] = min(dp[curr][prev] , solve(curr+1, i, first) + m[curr][i])

    return dp[curr][prev]
n = int(input())
m = [0]*n
for _ in range(n):
    m[_] = list(map(int,input().split()))
ret = int(1e9)
for i in range(3):
    dp = [[-1]*3 for _ in range(n)]
    ret = min(ret, solve(1,i,i) + m[0][i])
print(ret)