import sys
input = sys.stdin.readline

dp = [0]+[1]+[1]
n=int(input())
for i in range(n+1):
    dp.append(dp[-1]+dp[-2])
print(dp[n])