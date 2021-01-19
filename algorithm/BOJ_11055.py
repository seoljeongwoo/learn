import sys
input = sys.stdin.readline
N , A = int(input()) , list(map(int,input().split()))
dp = [0]*N
for i in range(N):
    for j in range(i-1,-1,-1):
        if A[i] > A[j] :
            dp[i] = max(dp[i], dp[j])
    dp[i] += A[i]
print(max(dp))