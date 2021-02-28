import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))
LIS = [lst[0]]
for _ in range(1,len(lst)):
    idx = bisect_left(LIS, lst[_])
    if idx == len(LIS):
        LIS.append(lst[_])
    else:
        LIS[idx] = lst[_]
print(len(LIS))