def hanoi(start , end, mid,n):
    if n == 0: return []
    return hanoi(start,mid,end,n-1) + [[start,end]] + hanoi(mid,end,start,n-1)

def solution(n):
    answer = hanoi(1,3,2,n)
    return answer
