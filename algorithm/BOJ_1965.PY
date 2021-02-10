import sys
from bisect import bisect_left
input = sys.stdin.readline
N ,lst = int(input()) ,list(map(int,input().split()))
LIS = [lst[0]]
for i in range(1,N):
    idx = bisect_left(LIS, lst[i])
    if idx>= len(LIS):
        LIS.append(lst[i])
    else:
        LIS[idx] = lst[i]
print(len(LIS))
