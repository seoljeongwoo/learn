import sys
import heapq
input = sys.stdin.readline
def dijkstra(st, en):
    pq = []
    INF = 100000*100000
    heapq.heappush(pq,(0,st))
    dist = [INF]*(N+1)
    dist[st] = 0
    while pq:
        curr_weight ,curr_node = heapq.heappop(pq)
        if dist[curr_node] < curr_weight: continue
        for next_node, next_weight in edge[curr_node]:
            if dist[next_node] > curr_weight + next_weight:
                heapq.heappush(pq, (curr_weight + next_weight , next_node))
                dist[next_node] = curr_weight + next_weight
    return dist[en]

N,M=int(input()), int(input())
edge = [ [] for _ in range(N+1)]
for _ in range(M):
    u,v,w= map(int,input().split())
    edge[u].append([v,w])
start,end=map(int,input().split())
print(dijkstra(start,end))