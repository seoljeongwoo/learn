import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
def RGB(curr,pre):
    if curr == N-1:
        return c[curr][pre]
    if dp[curr][pre] != -1:
        return dp[curr][pre]
    ret = 987654321 
    for i in range(3):
        if i == pre: continue
        ret = min(ret, RGB(curr+1,i))
    dp[curr][pre] = ret + c[curr][pre]
    return dp[curr][pre]
N =int(input())
c = [ list(map(int,input().split())) for _ in range(N) ]
dp = [[-1]*3 for _ in range(N)]
print(min(RGB(0,0) , RGB(0,1) ,RGB(0,2)))
