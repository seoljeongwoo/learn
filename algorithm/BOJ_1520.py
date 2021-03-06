import sys
sys.setrecursionlimit(501*501)
input = sys.stdin.readline
def check(x,y):
    return 0<=x<n and 0<=y<m
def solve(x,y):
    if x== n-1 and y==m-1: return 1
    if dp[x][y] != -1: return dp[x][y]
    ret = 0
    for dx,dy in direction:
        nx,ny= x+dx,y+dy
        if not check(nx,ny) or board[x][y] <= board[nx][ny]: continue
        ret += solve(nx,ny)
    dp[x][y] = ret
    return dp[x][y]
n,m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
dp = [[-1]*m for _ in range(n)]
direction = [(-1,0),(1,0),(0,1),(0,-1)]
print(solve(0,0))