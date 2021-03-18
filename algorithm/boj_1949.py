import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def dfs(curr, prev):

    for nx in edge[curr]:
        if nx == prev: continue
        tree[curr].append(nx); dfs(nx, curr)
    return

def solve(curr, include):
    if dp[include][curr] != -1: return dp[include][curr]
    dp[include][curr] = w[curr] if include else 0
    for nx in tree[curr]:
        if include:
            dp[include][curr] += solve(nx, False)
        else:
            left, right = solve(nx,True), solve(nx,False)
            dp[include][curr] += max(left, right)
    return dp[include][curr]

n = int(input())
w = [0]+list(map(int,input().split()))
edge =[ [] for _ in range(n+1)]
tree =[ [] for _ in range(n+1)]

for _ in range(n-1):
    u,v = map(int,input().split())
    edge[u].append(v); edge[v].append(u)
dfs(1,1)
dp = [[-1]*(n+1) for _ in range(2)]

left , right = solve(1,True), solve(1,False)
print(max(left, right))
