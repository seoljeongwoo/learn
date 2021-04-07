import sys
input = sys.stdin.readline
def solve(x,y,st):
    if len(st) == 0: return 1
    ret = 0
    for dx, dy in direction:
        nx, ny = x+dx , y+ dy
        if nx <0: nx += r
        if ny <0: ny += c
        nx%=r; ny%=c
        if m[nx][ny] == st[0]:
            ret += solve(nx,ny, st[1:])
    return ret
r,c,k = map(int,input().split())
m = [list(input().rstrip('\n')) for _ in range(r)]
direction = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
dp = {}
for _ in range(k):
    inp = input().rstrip('\n')
    if inp in dp.keys(): print(dp[inp])
    else:
        lst = list(inp)
        ret = 0
        for i in range(r):
            for j in range(c):
                if m[i][j] == lst[0]:
                    ret += solve(i,j,lst[1:])
        print(ret)
        dp[inp] = ret
