import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
print = sys.stdout.write
def solve(cp, lp,rp):
    if cp == w+1: return 0
    if dp[lp][rp] != -1: return dp[lp][rp]
    dp[lp][rp] = (1<<31)
    lpx,lpy = -1,-1
    rpx,rpy = -1,-1
    cpx,cpy = p[cp-1]

    if lp ==0: lpx,lpy =1,1
    else: lpx,lpy = p[lp-1]

    if rp ==0: rpx,rpy=n,n
    else: rpx,rpy = p[rp-1]

    left = solve(cp+1,cp,rp) + abs(cpx-lpx) + abs(cpy-lpy)
    right = solve(cp+1,lp,cp) + abs(cpx-rpx) + abs(cpy-rpy)
    if left > right:
        dp[lp][rp] = right
        path[lp][rp]=2
    else:
        dp[lp][rp] = left
        path[lp][rp]=1

    return dp[lp][rp]

def path_search(cp,lp,rp):
    while cp != w+1:
        lpx,lpy = -1,-1
        rpx,rpy = -1,-1
        cpx,cpy = p[cp-1][0],p[cp-1][1]

        if lp ==0: lpx,lpy =1,1
        else: lpx,lpy = p[lp-1][0],p[lp-1][1]

        if rp ==0: rpx,rpy=n,n
        else: rpx,rpy = p[rp-1][0], p[rp-1][1]

        if path[lp][rp] == 1: print(1);lp=cp
        else: print(2); rp=cp
        cp+=1
    return

n,w=int(input()),int(input())
p = [list(map(int,input().split())) for _ in range(w)]
dp = [[-1]*(w+1) for _ in range(w+1)]
path =[[-1]*(w+1) for _ in range(w+1)]
print(solve(1,0,0))
path_search(1,0,0)
