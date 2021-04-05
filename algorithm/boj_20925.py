import sys
input = sys.stdin.readline
def solve(curr, nt):
    if nt <= 0: return 0
    if dp[curr][nt] != -1: return dp[curr][nt]
    dp[curr][nt] = nt * exp[curr][1]
    for index in range(curr+1,n):
        gap = exp[index][0] - exp[curr][0]
        if exp[curr][1] == 0: continue
        nnt = gap//exp[curr][1] if gap%exp[curr][1] == 0 else gap//exp[curr][1] + 1
        dp[curr][nt] = max(dp[curr][nt] , gap + solve(index,nnt - time[curr][index]))
    return dp[curr][nt]
n,t = map(int,input().split())
dp = [[-1]*(t+1) for _ in range(n)]
exp = [list(map(int,input().split())) for _ in range(n)]
time = [list(map(int,input().split())) for _ in range(n)]
exp.sort()
inf = int(1e9)
ret = -inf
for index in range(n):
    if exp[index][0] == 0:
        ret = max(ret, solve(index, t))
print(ret)