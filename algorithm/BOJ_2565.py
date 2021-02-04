from bisect import bisect_left
import sys
input = sys.stdin.readline
N = int(input())
lst = []
for _ in range(N):
    lst.append(tuple(map(int,input().split())))
lst.sort()
result = [lst[0][1]]
for _ in range(1,N):
    if result[-1] < lst[_][1]: result.append(lst[_][1])
    else: pos = bisect_left(result , lst[_][1]); result[pos] = lst[_][1]
print(N-len(result))