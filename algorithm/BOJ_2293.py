import sys
input = sys.stdin.readline

n,k=map(int,input().split())
dp = [0]*(k+1)
dp[0]=1
for _ in range(n):
    v = int(input())
    for j in range(k+1):
        if j+v > k: break
        dp[j+v]+=dp[j]
print(dp[k])