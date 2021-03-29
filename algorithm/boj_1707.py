import sys
from collections import deque
input = sys.stdin.readline
def bfs(curr, paint):
    deq = deque()
    deq.append(curr)
    color[curr] = paint
    while deq:
        curr_node = deq.popleft()
        next_paint = 1 if color[curr_node] == 2 else 2
        for nx in graph[curr_node]:
            if color[nx] == 0 :
                color[nx] = next_paint
                deq.append(nx)
            elif color[nx] != next_paint: return False
    return True
t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    color = [0] * (n+1)
    graph = [ [] for _ in range(n+1)]
    for __ in range(m):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    ok = True
    for i in range(1,n+1):
        if color[i] == 0:
            ret = bfs(i,1)
        if ret == False:
            ok = ret
            break
    if ok: print("YES")
    else : print("NO")