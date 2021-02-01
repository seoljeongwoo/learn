import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def p(start, end):
    if start > end: 
        start,end = end,start
    if start == end: return 1
    if start+1 == end:
        if lst[start] == lst[end]: return 1
        else : return 0
        
    if DP[start][end] != -1:
        return DP[start][end]
    
    if lst[start] == lst[end]:
        DP[start][end] = p(start+1, end-1)
    else:
        DP[start][end] = 0
    return DP[start][end]

N , lst = int(input()) , [0] + list(map(int,input().split()))
M = int(input())
DP = [[-1]*(N+1) for _ in range(N+1)]
for _ in range(M):
    S,E = map(int,input().split())
    print(p(S,E))