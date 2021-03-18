import sys
import heapq
input = sys.stdin.readline
def solve(start,end):
    INF = (1<<31)
    dist = [INF] * (city+1)
    path = [ i for i in range(city+1)]
    pq = []
    heapq.heappush(pq, (0, start ,start))
    while pq:
        weight , curr_node, prev_node = heapq.heappop(pq)
        if dist[curr_node] != INF: continue
        dist[curr_node] = weight
        path[curr_node] = prev_node
        for next_node, edge_weight in edge[curr_node]:
            if dist[next_node] != INF: continue
            heapq.heappush(pq, (weight + edge_weight , next_node , curr_node))

    
    print(dist[end])

    visit_city = []
    while path[end] != end:
        visit_city.append(end)
        end = path[end]
    visit_city.append(end)
    print(len(visit_city))
    print(*visit_city[::-1])
    return
    
city , bus = int(input()) ,int(input())
edge = [ [] for _ in range(city+1)]
for _ in range(bus):
    u,v,w= map(int,input().split())
    edge[u].append((v,w))
start ,end = map(int , input().split())
solve(start,end)