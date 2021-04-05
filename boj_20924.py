import sys
from collections import deque
sys.setrecursionlimit(202020)
input = sys.stdin.readline
def bfs(start):
    q = deque()
    q.append(start)
    dist[start] = 0
    giga = -1
    while q:
        curr = q.popleft()
        if giga == -1 and len(edge[curr]) >= 2 : giga = curr
        if giga == -1 and curr != start and len(edge[curr]) == 0: giga = curr
        for nx, nw in edge[curr]:
            if dist[nx] != -1: continue
            dist[nx] = dist[curr] + nw
            q.append(nx)
    return giga
def construct(curr):
    v[curr] = True
    for nx , nw in bi_edge[curr]:
        if v[nx]: continue
        edge[curr].append((nx,nw))
        construct(nx)
    return 
n,r = map(int,input().split())
bi_edge = [ [] for _ in range(n+1)]
edge = [ [] for _ in range(n+1)]
for _ in range(n-1):
    u,v,w = map(int,input().split())
    bi_edge[u].append((v,w))
    bi_edge[v].append((u,w))
v = [False] * (n+1)
construct(r)

dist = [-1] * (n+1)
giga = bfs(r)

ret = 0
for i in range(1,n+1):
    ret = max(ret, dist[i])
print(dist[giga] , ret - dist[giga])