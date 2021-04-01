import sys
from collections import deque
input = sys.stdin.readline

def bfs(x,y,mdist,ro,rw):
    v = [-1] * (n+1)
    v[x] , v[y] = 0, 0
    que = deque()
    que.append(x); que.append(y)
    while que:
        curr = que.popleft()
        for nx in edge[curr]:
            if v[nx] != -1: continue
            v[nx] = v[curr] + 1
            que.append(nx)
    ss = sum(v[1:])
    if ss < mdist:
        return ss, x, y
    elif ss == mdist:
        if ro > x :
            return ss, x, y
        elif ro == x:
            if rw > y:
                return ss, x, y
    return mdist, ro, rw
n,m = map(int,input().split())
edge = [ [] for _ in range(n+1)]
for _ in range(m):
    u,v = map(int,input().split())
    edge[u].append(v)
    edge[v].append(u)

min_dist = 101*101
ret_one, ret_two = -1,-1
for i in range(1,n+1):
    for j in range(i+1, n+1):
        min_dist, ret_one, ret_two = bfs(i,j,min_dist,ret_one, ret_two)
print(ret_one, ret_two, 2*min_dist)