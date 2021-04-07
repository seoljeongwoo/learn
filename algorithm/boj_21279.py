import sys
import heapq
input = sys.stdin.readline
n,c = map(int,input().split())
edge = [ [] for _ in range(100001)]
for _ in range(n):
    x,y,v = map(int,input().split())
    edge[x].append((y,v))
q = []
total_cost = 0
ret = 0
for _ in range(100001):
    if len(edge[_]) ==0: continue
    for j in range(len(edge[_])):
        heapq.heappush(q,(-1*edge[_][j][0] , edge[_][j][1]))
        total_cost += edge[_][j][1]
    while len(q) >0 and len(q) > c:
        top_height, top_cost = heapq.heappop(q)
        total_cost -= top_cost
        while len(q) >0 and top_height == q[0][0]:
            pop_hegiht , pop_cost = heapq.heappop(q)
            total_cost -= pop_cost
    ret = max(ret, total_cost)
print(ret)