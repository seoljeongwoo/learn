import sys
from collections import deque
sys.setrecursionlimit(303030)
def solution(a, edges):
    
    answer = 0
    SZ = len(a)
    edge = [ [] for _ in range(SZ)]
    parent = [-1]*SZ
    inq = [0]*SZ
    
    for u,v in edges:
        edge[u].append(v)
        edge[v].append(u)
        
    def dfs(curr, prev):
        for nx in edge[curr]:
            if nx == prev: continue
            dfs(nx,curr)
            parent[nx] = curr
            inq[curr] += 1
        return
    
    dfs(0,-1)
    q = deque()
    for index, data in enumerate(inq):
        if data == 0 : q.append(index)
            
    while q :
        curr = q.popleft()
        answer += abs(a[curr])
        if parent[curr] != -1:
            a[parent[curr]] += a[curr]
            a[curr] = 0
            inq[parent[curr]] -= 1
            if inq[parent[curr]] == 0: q.append(parent[curr])
    
    if a[0] != 0 : answer = -1
    
    return answer
