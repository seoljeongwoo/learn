import sys
from collections import deque
input = sys.stdin.readline
N=int(input())
edge= [[] for _ in range(N+1)]
inq=[0]*(N+1)
build=[0]*(N+1)
dp=[0]*(N+1)
for _ in range(1,N+1):
    lst=list(map(int,input().split()))
    build[_]=lst[0]
    for j in range(1,len(lst)-1):
        inq[_]+=1;edge[lst[j]].append(_)
q=deque()
for _ in range(1,N+1):
    if inq[_]==0:q.append(_)
while q:
    c=q.popleft()
    dp[c]+=build[c]
    for nx in edge[c]:
        dp[nx]=max(dp[nx],dp[c]);inq[nx]-=1
        if inq[nx]==0: q.append(nx)
for _ in range(1,N+1):
    print(dp[_])