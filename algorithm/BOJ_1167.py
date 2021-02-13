import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
N = int(input())
edge = [ [] for _ in range(N+1)]
for _ in range(N):
    lst = list(map(int,input().split()))[0:-1]
    for i in range(1,len(lst),2):
        next_idx , weight = lst[i] , lst[i+1]
        edge[lst[0]].append((next_idx, weight))
def dfs(node, dist):
    if visited[node] != -1: return
    visited[node] = dist

    for next_node, weight in edge[node]:
        if visited[next_node] != -1: continue
        dfs(next_node, dist + weight)
    return

visited = [-1] * (N+1)
dfs(1,0)
max_value = max(visited)
start = 0
for index, value in enumerate(visited):
    if max_value == value:
        start=  index
        break
visited = [-1] * (N+1)
dfs(start,0)
print(max(visited))
    