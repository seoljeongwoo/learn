import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
N = int(input())
edge = [ [] for _ in range(N+1)]
for _ in range(N-1):
    u,v,w=map(int,input().split())
    edge[u].append((v,w))
    edge[v].append((u,w))
def dfs(curr,dist):
    global max_dist, max_index
    if max_dist < dist:
        max_dist = dist
        max_index = curr

    if visited[curr] == True: return
    visited[curr] = True

    for next_index , weight in edge[curr]:
        if visited[next_index] == True: continue
        dfs(next_index, dist + weight)
    return

max_dist , max_index = -1,-1
visited = [False] * (N+1)
dfs(1,0)
visited = [False] * (N+1)
dfs(max_index,0)
print(max_dist)
