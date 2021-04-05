import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int,input().split())
lst = deque([i+1 for i in range(n)])
ret = []
while lst:
    if k>= len(lst)-1:
        ret.append(lst.pop())
        k-= len(lst)
    else:
        ret.append(lst.popleft())
print(*ret)