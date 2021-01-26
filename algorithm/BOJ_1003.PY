import sys
input = sys.stdin.readline
DP = [(1,0)] + [(0,1)]
for i in range(40):
    DP.append((DP[-2][0] + DP[-1][0] , DP[-2][1] + DP[-1][1]))
T = int(input())
for _ in range(T):
    print(*DP[int(input())])