def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    low , high = 1, distance
    while low <= high:
        mid = (low+high) // 2
        cnt , prev = 0, 0
        for index, value in enumerate(rocks):
            if rocks[index] - prev < mid:
                cnt += 1
            else:
                prev = rocks[index]
        
        if cnt <= n: 
            answer = mid
            low = mid+1
        else:
            high = mid-1
    return answer
