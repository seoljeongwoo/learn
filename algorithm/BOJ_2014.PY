import heapq

K,N = map(int,input().split())
p = list(map(int,input().split()))
lst , st = [], set()
for i in p:
    lst.append(i)
heapq.heapify(lst)

for _ in range(N-1):
    t = heapq.heappop(lst)
    for d in p:
        heapq.heappush(lst,d*t)
        if t%d==0:
            break
print(lst[0])
