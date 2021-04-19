import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))

ans = 0
for data in list(permutations([i for i in range(n)],n)):
    ret = 0
    for i in range(1,n):
        ret += abs(lst[data[i-1]] - lst[data[i]])
    ans = max(ans, ret)
print(ans)