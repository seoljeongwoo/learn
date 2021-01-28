import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def stair(curr,prev):
    if curr > N or prev >=3:
        return -987654321
    if curr == N:
        if prev == 3:
            return -987654321
        else:
            return lst[curr]
    if dp[curr][prev] != -1:
        return dp[curr][prev]
    ret = -987564321
    ret = max(ret,stair(curr+1,prev+1))
    ret = max(ret, stair(curr+2,1))
    dp[curr][prev] = ret
    if dp[curr][prev] != -987654321:
        dp[curr][prev] += lst[curr]
    return dp[curr][prev]

N = int(input())
lst = [0] + [ int(input()) for _ in range(N)]
dp = [ [-1]*4 for _ in range(N+1)]
print(stair(0,0))