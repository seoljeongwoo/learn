def solution(n, k):
    answer = []
    k -= 1
    fac = [1 for i in range(n)]
    for i in range(1,n): fac[i] = i*fac[i-1]
    used = [i for i in range(1,n+1)]
    while n > 0 :
        target = 0
        if fac[n-1] <= k:
            target = k//(fac[n-1])
            k -= target * fac[n-1]
        print(target)
        answer.append(used[target])
        del used[target]
        n-=1
            
    return answer
