import sys
sys.setrecursionlimit(101010)
input = sys.stdin.readline
def solve(curr):
    if curr >= n: return 0
    if curr in dp.keys(): return dp[curr]
    dp[curr] = solve(curr+1)
    if p[curr] != -1: dp[curr] = max(dp[curr], solve(np[curr]) + p[curr])
    return dp[curr]

n,k=map(int,input().split())
lst = list(map(int,input().split()))
p = [-1]*n
np = [0]*n
i,j,s=0,0,0
while i<n:
    if s < k:
        s += lst[i]
        i+=1
    else:
        p[j] = s-k
        np[j] = i
        s -= lst[j]
        j+=1
while j<n:
    if s>=k:
        p[j] = s-k
        np[j] = i
        s -= lst[j]
        j+=1
    else:
        break
dp = {}
print(solve(0))