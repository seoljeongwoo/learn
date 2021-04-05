import sys
input = sys.stdin.readline
def solve(curr, bit):
    if curr > n: return 0
    if curr == n:
        if bit == 0 : return 1
        else: return 0
    if dp[curr][bit] != -1: return dp[curr][bit]
    dp[curr][bit] = 0
    if bit == 0:
        dp[curr][bit] += solve(curr+2, 0)
        dp[curr][bit] += solve(curr+1, 4)
        dp[curr][bit] += solve(curr+1, 1)
    elif bit == 1:
        dp[curr][bit] += solve(curr+1, 0)
        dp[curr][bit] += solve(curr+1, 6)
    elif bit == 4:
        dp[curr][bit] += solve(curr+1,0)
        dp[curr][bit] += solve(curr+1,3)
    elif bit == 3:
        dp[curr][bit] += solve(curr+1,4)
    elif bit == 6:
        dp[curr][bit] += solve(curr+1,1)
    return dp[curr][bit]
n = int(input())
dp = [[-1]*(8) for _ in range(n+1)] 
print(solve(0,0))