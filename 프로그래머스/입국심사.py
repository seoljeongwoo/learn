def solution(n, times):
    answer = 0
    low , high = 0, int(1e9) * int(1e9) + 1
    while low <= high:
        mid = (low + high) // 2
        
        process = 0
        for time in times: process += (mid // time)
            
        if process >= n:
            answer = mid
            high = mid-1
        else:
            low = mid +1
    
    return answer
