import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def solve(curr):
    dp[curr] = 0
    ret = 0
    for nx in edge[curr]:
        if dp[nx] != -1: continue
        ret += solve(nx)
    
    dp[curr] = ret+1
    return dp[curr]


n,r,q = map(int,input().split())
edge = [ [] for _ in range(n+1)]
for _ in range(n-1):
    u,v=map(int,input().split())
    edge[u].append(v)
    edge[v].append(u)
dp = [-1] * (n+1)
solve(r)
for _ in range(q):
    print(dp[int(input())])