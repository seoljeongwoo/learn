import sys
input = sys.stdin.readline
N,M=map(int,input().split())
lst = [ list(map(int,input().split())) for _ in range(N)]
DP = [0]*M
DP[0] = lst[0][0]
for i in range(1,M):
    DP[i] = DP[i-1] + lst[0][i]
for i in range(1,N):
    left_DP , right_DP = [0]*M ,[0]*M
    left_DP[0] = DP[0] + lst[i][0]
    for j in range(1,M):
        left_DP[j] = max(left_DP[j-1] , DP[j]) + lst[i][j]
    right_DP[M-1] = DP[M-1] + lst[i][M-1]
    for j in range(M-2,-1,-1):
        right_DP[j] = max(right_DP[j+1] , DP[j]) + lst[i][j]
    for j in range(M):
        DP[j] = max(left_DP[j], right_DP[j])
print(DP[M-1])