import sys
import heapq
input = sys.stdin.readline
def dijkstra(start,edge):
    dist = [float('inf')] * (N+1)
    queue = []
    heapq.heappush(queue, (0,start))
    while queue:
        curr_dist, curr_node = heapq.heappop(queue)
        if dist[curr_node] != float('inf') : continue
        dist[curr_node] = curr_dist

        for next_node, weight in edge[curr_node]:
            if dist[next_node] != float('inf') : continue
            heapq.heappush(queue, (curr_dist + weight , next_node))
    return dist

N,M,X= map(int,input().split())
go_edge = [ [] for _ in range(N+1)]
back_edge = [ [] for _ in range(N+1)]
for _ in range(M):
    u,v,w=map(int,input().split())
    go_edge[u].append((v,w))
    back_edge[v].append((u,w))

go_dist = dijkstra(X,go_edge)
back_dist = dijkstra(X,back_edge)
result = 0
for i in range(1,N+1):
    if i==X: continue
    result = max(result, go_dist[i] + back_dist[i])

print(result)
