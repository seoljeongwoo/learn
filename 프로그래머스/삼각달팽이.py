def solution(n):
    answer = []
    array = [[0] * n for n in range(1,n+1)]
    size , curr = n , 1
    up, down , left, right = 0, n , 0 , n
    while size>0 :
        for i in range(size):
            array[up+i][left] = curr
            curr +=1
        
        for i in range(size-1):
            array[down-1][left+1+i] = curr
            curr +=1
        
        for i in range(size-2):
            array[down-2-i][right-2-i] = curr
            curr += 1
            
        up , down, left, right = up +2 , down -1 , left +1, right -2
        size -= 3
    
    for i in range(n):
        for j in range(i+1):
            answer.append(array[i][j])
    return answer
