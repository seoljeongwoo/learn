import sys
import heapq
input = sys.stdin.readline

def check(wei):
    q = []
    dist = [inf]*(n+1)
    heapq.heappush(q,(0,a))
    while q:
        curr_weight, curr_node = heapq.heappop(q)
        if dist[curr_node] != inf: continue
        dist[curr_node] = curr_weight
        for next_node, next_weight in edge[curr_node]:
            if dist[next_node] != inf: continue
            if next_weight > wei: continue
            heapq.heappush(q,(curr_weight + next_weight, next_node))
    return dist[b] <= c
inf = int(1e16)+5
n,m,a,b,c = map(int,input().split())
edge = [ [] for _ in range(n+1)]
lo = int(1e9)
hi = -int(1e9)
for _ in range(m):
    u,v,w= map(int,input().split())
    lo = min(lo,w)
    hi = max(hi,w)
    edge[u].append((v,w))
    edge[v].append((u,w))
ret = -1
while lo<=hi:
    mid = (lo+hi)//2
    if check(mid) : 
        ret = mid
        hi = mid-1
    else:
        lo = mid+1
print(ret)
