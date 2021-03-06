import sys
input = sys.stdin.readline
def dist(a,b):
    return ((xy[a][0]-xy[b][0])**2+(xy[a][1]-xy[b][1])**2)**0.5
def solve(c,v):
    if v == (1<<N)-1 : return w[c][0]
    if dp[c][v] != -1 : return dp[c][v]
    ret = float('inf')
    for x in range(N):
        if v&(1<<x): continue
        ret = min(ret, solve(x,v|(1<<x))+w[c][x])
    dp[c][v]=ret
    return dp[c][v]
N =int(input())
xy = [list(map(int,input().split())) for _ in range(N)]
w = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        w[i][j] = dist(i,j)
dp = [[-1]*(1<<N) for _ in range(N)]
print(solve(0,1))