import sys
sys.setrecursionlimit(101010)
input = sys.stdin.readline

def dfs_tree(curr):
    for nx in edge[curr]:
        if depth[nx] != -1: continue
        depth[nx] =depth[curr] + 1
        sp[nx][0] = curr
        dfs_tree(nx)
    return

def lca( u , v ):
    if depth[u] < depth[v] : u,v = v,u
    diff = depth[u] - depth[v]
    for i in range(maxn):
        if diff & (1<<i): u = sp[u][i]
    if u==v : return u

    for i in range(maxn-1, -1 ,-1 ):
        if sp[u][0] != -1 and (sp[u][i] != sp[v][i]):
            u = sp[u][i]
            v = sp[v][i]
    return sp[u][0]

maxn = 17
N = int(input())
sp = [[-1] * maxn for _ in range(N+1)]
edge = [ [] for _ in range(N+1)]
depth = [-1] * (N+1)
for _ in range(N-1):
    u,v = map(int,input().split())
    edge[u].append(v)
    edge[v].append(u)

depth[1] = 0
dfs_tree(1)

for j in range(1,maxn):
    for i in range(1,N+1):
        if sp[i][j-1] != -1 : sp[i][j] = sp[sp[i][j-1]][j-1]

M = int(input())
for _ in range(M):
    u,v = map(int,input().split())
    print(lca(u,v))