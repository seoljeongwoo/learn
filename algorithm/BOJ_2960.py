import sys
input = sys.stdin.readline
N,K=map(int,input().split())
is_prime = [False]*(N+1)
result , cnt = -1, 0
for i in range(2,N+1):
    for j in range(i,N+1,i):
        if is_prime[j] == False:
            is_prime[j] = True
            cnt +=1
            if cnt == K : result = j
print(result)