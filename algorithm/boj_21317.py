import sys
input = sys.stdin.readline
def solve(curr, ok):
    if curr > n : return inf
    if curr == n: return 0
    if dp[curr][ok] != inf: return dp[curr][ok]
    dp[curr][ok] = solve(curr+1,ok) + jump[curr][0]
    dp[curr][ok] = min(dp[curr][ok] , solve(curr+2,ok) + jump[curr][1])
    if ok: dp[curr][ok] = min(dp[curr][ok] , solve(curr+3,ok-1) + k)
    return dp[curr][ok]
n = int(input())
jump = [[0]*2 for _ in range(n)]
for _ in range(n-1):
    small, big = map(int,input().split())
    jump[_+1][0] , jump[_+1][1] = small, big
k = int(input())
inf = int(1e9)+5
dp = [[inf]*2 for _ in range(n+1)]
print(solve(1,1))