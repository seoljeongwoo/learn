import sys
import math
sys.setrecursionlimit(40000+5)
input = sys.stdin.readline

def dfs_tree(curr):

    for nx, wei in edge[curr]:
        if depth[nx] != -1: continue
        depth[nx] = depth[curr] + 1
        parent_table[nx][0] = curr
        weight_table[nx][0] = wei
        dfs_tree(nx)
    return

def lca(u,v):

    ret = 0

    if depth[u] < depth[v] : u,v = v, u
    diff = depth[u] - depth[v]
    for i in range(MaxN):
        if diff & (1<<i): 
            ret += weight_table[u][i]
            u = parent_table[u][i]
    
    if u==v: return ret
    for i in range(MaxN-1 , -1 ,-1):
        if parent_table[u][i] != parent_table[v][i]:
            ret += (weight_table[u][i] + weight_table[v][i])
            u = parent_table[u][i]
            v = parent_table[v][i]
    
    return ret + weight_table[u][0] + weight_table[v][0]

N = int(input())
MaxN = math.ceil(math.log2(N))
edge = [ [] for _ in range(N+1)]
depth = [-1] * (N+1)
parent_table = [[0]*MaxN for _ in range(N+1)]
weight_table = [[0]*MaxN for _ in range(N+1)]
for _ in range(N-1):
    u,v,w = map(int,input().split())
    edge[u].append((v,w))
    edge[v].append((u,w))

depth[1] = 0
dfs_tree(1)

for j in range(1,MaxN):
    for i in range(1,N+1):
        parent_table[i][j] = parent_table[parent_table[i][j-1]][j-1]
        weight_table[i][j] = weight_table[i][j-1] + weight_table[parent_table[i][j-1]][j-1]

M = int(input())
for _ in range(M):
    u , v = map(int,input().split())
    print(lca(u,v))
