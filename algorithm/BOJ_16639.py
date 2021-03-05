import sys
input = sys.stdin.readline
def cal(a,b,op):
    if op=='+': return a+b
    elif op=='-': return a-b
    else : return a*b
def solve():
    for i in range(M):
        max_dp[i][i] = lst[i*2]
        min_dp[i][i] = lst[i*2]
    
    for k in range(1,M):
        for i in range(M-k):
            j=i+k
            for x in range(i,j):
                op = lst[2*x+1]
                a = cal(max_dp[i][x],max_dp[x+1][j],op)
                b = cal(max_dp[i][x],min_dp[x+1][j],op)
                c = cal(min_dp[i][x],max_dp[x+1][j],op)
                d = cal(min_dp[i][x],min_dp[x+1][j],op)
                max_dp[i][j] = max(max_dp[i][j],a,b,c,d)
                min_dp[i][j] = min(min_dp[i][j],a,b,c,d)
    return max_dp[0][-1]

N =int(input())
lst = list(input())
for i in range(N):
    if '0'<=lst[i]<='9': lst[i] = ord(lst[i])-ord('0')
INF = (1<<32)
M = N//2 +1
max_dp = [ [-INF]*M for _ in range(M)]
min_dp = [ [INF]*M for _ in range(M)]
print(solve())
