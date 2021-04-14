import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def solve(curr, s):

    if curr == n-1:
        if s==lst[-1]: return 1
        else: return 0
    
    if dp[curr][s] != -1: return dp[curr][s]
    dp[curr][s] = 0
    if s+lst[curr] <=20: dp[curr][s] += solve(curr+1,s+lst[curr])
    if s-lst[curr] >=0 : dp[curr][s] += solve(curr+1,s-lst[curr])
    return dp[curr][s]

n = int(input())
lst = list(map(int,input().split()))
dp = [[-1]*21 for _ in range(n)]
print(solve(1,lst[0]))