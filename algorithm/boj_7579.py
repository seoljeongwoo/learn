import sys
input = sys.stdin.readline
 
n,m=map(int,input().split())
memory = list(map(int,input().split()))  
cost = list(map(int,input().split()))
total_cost = sum(cost)
dp = [0]*(total_cost + 1)
for _ in range(n):
    for j in range(total_cost , cost[_]-1, -1):
        dp[j] = max(dp[j], dp[j-cost[_]] + memory[_])
result = 0
for _ in range(total_cost+1):
    if dp[_] >=m:
        result = _; break
print(result)