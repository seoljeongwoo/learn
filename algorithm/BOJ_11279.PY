import sys
import heapq
input = sys.stdin.readline

N = int(input())
queue = []
for _ in range(N):
    v = int(input())
    if v:
        heapq.heappush(queue, -v)
    else:
        if queue: print(-queue[0]); heapq.heappop(queue)
        else: print(0)
