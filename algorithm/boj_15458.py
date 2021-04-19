import sys
sys.setrecursionlimit(303030)
input = sys.stdin.readline

def dfs_tree(curr):
    visit[curr] = True
    for nx in edge[curr]:
        if visit[nx]: continue
        tree[curr].append(nx)
        dfs_tree(nx)
    return

def solve(curr, paint):
    if dp[curr][paint] != -1: return dp[curr][paint]

    if c[curr] != -1 and c[curr] != paint: return 0

    dp[curr][paint] = 1
    if len(tree[curr]) == 0: 
        return dp[curr][paint]

    if paint == 0:
        for nx in tree[curr]:
            if c[nx] == paint: 
                dp[curr][paint] = 0 
                break
            dp[curr][paint] *= (solve(nx,1) + solve(nx,2))
            dp[curr][paint]%=mod
    elif paint == 1:
        for nx in tree[curr]:
            if c[nx] == paint:
                dp[curr][paint] = 0
                break
            dp[curr][paint] *= (solve(nx,0) + solve(nx,2))
            dp[curr][paint]%=mod
    else:
        for nx in tree[curr]:
            if c[nx] == paint:
                dp[curr][paint] = 0
                break
            dp[curr][paint] *= (solve(nx,0) + solve(nx,1))
            dp[curr][paint]%=mod
    dp[curr][paint] %= mod
    return dp[curr][paint]

n,k = map(int,input().split())
edge = [ [] for _ in range(n+1)]
tree = [ [] for _ in range(n+1)]
mod = int(1e9) + 7

for _ in range(n-1):
    u,v = map(int,input().split())
    edge[u].append(v)
    edge[v].append(u)

visit = [False] * (n+1)
dfs_tree(1)
c = [-1] * (n+1)

for _ in range(k):
    u ,v = map(int,input().split())
    c[u] = v-1

dp = [[-1]*3 for _ in range(n+1)]
ret = 0
for i in range(3):
    ret += solve(1,i)
    ret %= mod
print(ret)