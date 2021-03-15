import sys
from collections import deque
def solve(subin, brother):
    INF = 200000
    dist = [-1]*(INF+1)
    q = deque()
    q.append(subin)
    dist[subin] = 0
    while q:
        curr = q.popleft()
        if curr+1 <= INF and dist[curr+1] == -1 : 
            q.append(curr+1); dist[curr+1] = dist[curr] + 1
        if curr-1 >=0 and dist[curr-1] == -1:
            q.append(curr-1); dist[curr-1] = dist[curr] + 1
        if curr*2 <= INF and dist[curr*2] == -1:
            q.append(curr*2); dist[curr*2] = dist[curr] + 1
    target = dist[brother]
    print(target)
    path_print = []

    while brother != subin:
        if dist[brother-1] +1 == dist[brother]: path_print.append(brother); brother = brother -1
        elif dist[brother+1]+1 == dist[brother]: path_print.append(brother); brother = brother +1
        else: path_print.append(brother); brother = brother//2
    path_print.append(subin)
    print(*path_print[::-1])
n,k = map(int,input().split())
solve(n,k)
