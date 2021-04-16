def solution(a):
    answer = 0
    size = len(a)
    
    left , right = [0]*size , [0]*size
    for i in range(size):
        if i==0:
            left[0] = a[0]
            right[size-1] = a[size-1]
        else:
            left[i] = min(left[i-1] , a[i])
            right[size-i-1] = min(right[size-i],a[size-i-1])
    
    for i in range(size):
        if a[i] == left[i] or a[i] == right[i]: answer +=1
            
    return answer
