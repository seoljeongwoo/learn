import sys
input = sys.stdin.readline
DP = [1,1,1,2,2]
for i in range(96):
    DP.append(DP[i] + DP[-1])
T =int(input())
for _ in range(T):
    print(DP[int(input())-1])