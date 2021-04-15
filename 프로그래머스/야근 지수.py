import heapq
def solution(n, works):
    answer = 0
    pq = []
    for work in works:
        heapq.heappush(pq,-1*work)
    for _ in range(n):
        if len(pq) == 0 : break
        top = -1*heapq.heappop(pq)
        top -= 1
        if top > 0: heapq.heappush(pq, -1*top)
    for data in pq:
        answer += data**2
    return answer
