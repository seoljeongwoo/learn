import sys
input = sys.stdin.readline
DP = [[1]*31 for _ in range(31)]
for i in range(1,31):
    for j in range(i,31):
        DP[i][j] = sum(DP[i-1][i-1:j])
T = int(input())
for _ in range(T):
    a,b=map(int,input().split())
    print(DP[a][b])
