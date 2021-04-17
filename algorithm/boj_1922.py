import sys
import heapq
input = sys.stdin.readline
def find(u):
    if parent[u] != u: parent[u] = find(parent[u])
    return parent[u]
def merge(u,v):
    u , v = find(u) , find(v)
    if u==v: return False
    parent[u] = v
    return True
N ,M  = int(input()) , int(input())
parent = [ i for i in range(N+1)]
pq = []
for _ in range(M):
    u,v,w = map(int,input().split())
    heapq.heappush(pq, (w,u,v))
ret , pick = 0, 0
while pq:
    w,u,v = heapq.heappop(pq)
    if merge(u,v):
        pick +=1
        ret += w
    if pick == N-1: break
print(ret)