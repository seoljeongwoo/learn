from collections import deque
def solution(n, vertex):
    answer = 0
    edge = [ [] for _ in range(n+1)]
    for u,v in vertex:
        edge[u].append(v)
        edge[v].append(u)
    vis = [-1] * (n+1)
    q = deque([1])
    vis[1] = 0

    while q:
        curr = q.popleft()
        for nx in edge[curr]:
            if vis[nx] != -1: continue
            q.append(nx)
            vis[nx] = vis[curr] +1
    mn = max(vis)
    for index in range(1,n+1):
        if mn == vis[index] : answer += 1
    return answer
