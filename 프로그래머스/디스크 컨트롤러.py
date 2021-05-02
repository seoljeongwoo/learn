import heapq
def solution(jobs):
    answer , SZ = 0, len(jobs)
    jobs.sort()
    time , index = jobs[0][0] , 0
    pq = []
    
    while index < SZ:
        if time == jobs[index][0]: 
            heapq.heappush(pq, ( jobs[index][1] , jobs[index][0]))
            index += 1
        else:
            break

    while pq:
        curr = heapq.heappop(pq)
        answer = answer + (time - curr[1] + curr[0])
        print(answer)
        time += curr[0]
        
        while index < SZ:
            if time >= jobs[index][0]:
                heapq.heappush(pq, (jobs[index][1] , jobs[index][0]))
                index += 1
            else:
                break
        
        if len(pq) == 0 and index < SZ:
            time = jobs[index][0]
            while index < SZ:
                if time == jobs[index][0] :
                    heapq.heappush(pq, (jobs[index][1] , jobs[index][0]))
                    index += 1
                else:
                    break
                    
    answer //= SZ
    return answer
