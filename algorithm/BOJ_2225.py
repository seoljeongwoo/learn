import sys
sys.setrecursionlimit(40404)
input = sys.stdin.readline
def solve(a,b):
    if a==0 : return 1
    if b==0: return 0
    if dp[a][b] != -1: return dp[a][b]
    dp[a][b] = 0
    l = min(a+1,n+1)
    for _ in range(0,l):
        dp[a][b] += solve(a-_,b-1)
        dp[a][b]%=MOD
    return dp[a][b]
MOD =int(1e9)
n,k=map(int,input().split())
dp =[[-1]*(k+1) for _ in range(n+1)]
print(solve(n,k))
