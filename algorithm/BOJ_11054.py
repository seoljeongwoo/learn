import sys
from bisect import bisect_left
input = sys.stdin.readline

N , lst = int(input()), list(map(int,input().split()))
LIS = []
DP = [0] * N
for i in range(N):
    idx = bisect_left(LIS, lst[i])
    if len(LIS) <= idx:
        LIS.append(lst[i])
        DP[i] = len(LIS)
    else:
        LIS[idx] = lst[i]
        DP[i]= idx+1
LIS = []
for i in range(N-1,-1,-1):
    idx = bisect_left(LIS , lst[i])
    if len(LIS) <= idx:
        LIS.append(lst[i])
        DP[i] += len(LIS)
    else:
        LIS[idx] = lst[i]
        DP[i] += idx+1
print(max(DP)-1)
