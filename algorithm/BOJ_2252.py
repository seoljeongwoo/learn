import sys
from collections import deque
input = sys.stdin.readline

N,M=map(int,input().split())
edge=[[] for _ in range(N+1)]
inq=[0]*(N+1)
for _ in range(M):
    u,v=map(int,input().split())
    edge[u].append(v)
    inq[v]+=1
q=deque()
for _ in range(1,N+1):
    if inq[_]==0:q.append(_)
lst = []
while q:
    c=q.popleft()
    lst.append(c)
    for n in edge[c]:
        inq[n]-=1
        if inq[n]==0:q.append(n)
for _ in range(1,N+1):
    if inq[_]>0:lst.append(_)
print(*lst)