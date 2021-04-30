def solution(n):
    if n <= 2: return n
    a,b,MOD = 1,2,1234567
    for i in range(3,n+1):
        a,b = b%MOD, (a+b)%MOD
    answer = b
    return answer
