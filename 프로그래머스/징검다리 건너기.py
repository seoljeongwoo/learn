def possible(mid, stones, k):
    presum = []
    if stones[0] >= mid : presum.append(0)
    else: presum.append(1)
    
    SZ = len(stones)
    for i in range(1,SZ):
        if stones[i] >= mid : presum.append(0)
        else: presum.append(presum[-1] + 1)
    return k > max(presum) 

def solution(stones, k):
    answer = 0
    low, high = 0 , 200000001
    while low < high:
        mid = (low + high) // 2
        if possible(mid, stones , k):
            answer = mid
            low = mid + 1
        else:
            high = mid
    return answer
