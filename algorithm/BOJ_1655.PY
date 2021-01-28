import heapq
import sys
input = sys.stdin.readline

N = int(input())
lq,mp=[],[]
for _ in range(N):
    v = int(input())
    if len(lq) == len(mp):
        if len(mp) ==0 or mp[0] >= v:
            heapq.heappush(lq,-v)
        else:
            heapq.heappush(lq,-mp[0])
            heapq.heapreplace(mp,v)
    else:
        if -lq[0] > v:
            heapq.heappush(mp, -lq[0])
            heapq.heapreplace(lq,-v)
        else:
            heapq.heappush(mp, v)
    print(-lq[0])