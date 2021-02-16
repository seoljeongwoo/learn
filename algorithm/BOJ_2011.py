import sys
sys.setrecursionlimit(10**5)
def solve(st):
    N = len(st)
    if N == 0: return 1
    if DP[N] != -1: return DP[N]

    DP[N] = 0
    num = int(st[0])
    if 1<=num<=26: DP[N] = solve(st[1:])%MOD
    else: return DP[N]
    if N>1 and 1<=int(st[:2])<=26: DP[N] = (DP[N]+solve(st[2:]))%MOD
    return DP[N]
try:
    S = input()
    MOD = 1000000
    DP = [-1] * (len(S)+1)
    print(solve(S))
except:
    print(0)
