import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

def dfs(curr, prev):
    for nx in edge[curr]:
        if nx == prev: continue
        dfs_edge[curr].append(nx)
        dfs(nx,curr)
    return

def solve(curr, pick):
    if dp[pick][curr] != -1: return dp[pick][curr]
    dp[pick][curr] = w[curr] if pick  else 0
    if pick:
        for nx in dfs_edge[curr]:
            dp[pick][curr] += solve(nx,False)
    else:
        for nx in dfs_edge[curr]:
            l = solve(nx,True)
            r = solve(nx,False)
            if l > r:
                path[nx] = True
            else:
                path[nx] = False

            dp[pick][curr] += max(l,r)
    return dp[pick][curr]

def trace(curr, pick):
    if pick:
        path_result.append(curr)
        for nx in dfs_edge[curr]:
            trace(nx, False)
    else:
        for nx in dfs_edge[curr]:
            trace(nx,path[nx])

    return

n = int(input())
w = [0] + list(map(int,input().split()))

edge = [[] for _ in range(n+1)]
dfs_edge =[ [] for _ in range(n+1)]
path_result = []

for _ in range(n-1):
    u,v = map(int,input().split())
    edge[u].append(v)
    edge[v].append(u)

dfs(1,-1)
dp = [[-1]*(n+1) for _ in range(2)]
path = [False] * (n+1)

l , r = solve(1,False) , solve(1,True)
if l<r: path[1] = True
else: path[1] = False
trace(1,path[1])

print(max(l,r))
path_result.sort()
print(*path_result)
