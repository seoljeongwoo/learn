import sys
import heapq
input = sys.stdin.readline

def dijkstra():
    pq = []
    heapq.heappush(pq, (0,1))
    dist[1].append(0)
    while pq:
        curr_weight, curr_node = heapq.heappop(pq)
        
        for next_node, next_weight in edge[curr_node]:
            if len(dist[next_node]) < k:
                heapq.heappush(dist[next_node] , -1*(curr_weight + next_weight))
                heapq.heappush(pq, (curr_weight + next_weight , next_node))
            else:
                if -1*dist[next_node][0] > curr_weight + next_weight:
                    heapq.heappop(dist[next_node])
                    heapq.heappush(dist[next_node] , -1*(curr_weight + next_weight))
                    heapq.heappush(pq, (curr_weight + next_weight , next_node))

    return

n,m,k = map(int,input().split())
edge = [ [] for _ in range(n+1)]
dist = [ [] for _ in range(n+1)]
for _ in range(m):
    u,v,w = map(int,input().split())
    edge[u].append((v,w))
dijkstra()
for i in range(1,n+1):
    if len(dist[i]) <k: print(-1)
    else: print(-1*dist[i][0])
