import sys
input = sys.stdin.readline

dp=[1]*10
n=int(input())
for i in range(1,n):
    for j in range(1,10):
        dp[j]=(dp[j]+dp[j-1])%10007
print(sum(dp)%10007)