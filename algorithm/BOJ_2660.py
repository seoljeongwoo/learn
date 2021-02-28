import sys
from collections import deque
input = sys.stdin.readline
def bfs(start):
    visit = [-1] * (N+1)
    Q = deque()
    Q.append(start)
    visit[start] = 0
    while Q:
        curr = Q.popleft()
        for nx in edge[curr]:
            if visit[nx] != -1: continue
            visit[nx] = visit[curr] + 1
            Q.append(nx)
    return visit

N = int(input())
edge = [ [] for _ in range(N+1)]
while True:
    u,v=map(int,input().split())
    if u==-1 and v==-1: break
    edge[u].append(v)
    edge[v].append(u)

point = [0] * (N+1)
min_value = 51
min_count = 0
for i in range(1,N+1):
    
    visit = bfs(i)
    point[i] = max(visit[1:])
    if min_value == point[i]:
        min_count += 1
    elif min_value > point[i]:
        min_value = point[i]
        min_count = 1

print(min_value, min_count)
for i in range(1,N+1):
    if min_value == point[i]:
        print(i , end=" ")
