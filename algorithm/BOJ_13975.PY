import heapq
import sys
input = sys.stdin.readline
TC= int(input())
for _ in range(TC):
    K = int(input())
    queue = []
    lst=  map(int, input().split())
    for data in lst:
        heapq.heappush(queue, data)
    total = 0
    while len(queue) >1 :
        fr = heapq.heappop(queue)
        se = heapq.heappop(queue)
        total += (fr+se)
        heapq.heappush(queue, fr+se)
    print(total)