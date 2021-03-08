import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n,k=map(int,input().split())
    inq=[0]*n
    edge=[[] for _ in range(n)]
    build = list(map(int,input().split()))
    for __ in range(k):
        u,v=map(int,input().split())
        u-=1;v-=1
        edge[u].append(v)
        inq[v]+=1
    target=int(input())
    q=deque()
    for __ in range(n):
        if inq[__]==0:q.append(__)
    dp=[0]*n
    while q:
        curr=q.popleft()
        dp[curr]+=build[curr]
        if curr==target-1:break
        for nx in edge[curr]:
            inq[nx]-=1;dp[nx]=max(dp[nx],dp[curr])
            if inq[nx]==0:q.append((nx))
    print(dp[target-1])