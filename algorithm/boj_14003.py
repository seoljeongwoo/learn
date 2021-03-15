import sys
from bisect import bisect_left
input = sys.stdin.readline
n = int(input())
lst = list(map(int,input().split()))
lis , path = [], [0]*n
for _ in range(n):
    idx = bisect_left(lis, lst[_])
    if len(lis) == idx: lis.append(lst[_]); path[_] = idx
    else: lis[idx] = lst[_] ; path[_] = idx
target = len(lis)-1
print(target+1)
path_print = []
for _ in range(n-1,-1,-1):
    if target == path[_]: path_print.append(lst[_]) ; target-=1
path_print = path_print[::-1]
print(*path_print)