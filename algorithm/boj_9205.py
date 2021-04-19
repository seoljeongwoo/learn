import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    lst = [list(map(int,input().split())) for _ in range(n+2)]
    q = deque([0])
    v = [False] * len(lst)
    v[0] = True
    while q:
        curr = q.popleft()
        for i in range(len(lst)):
            if v[i] : continue
            if abs(lst[curr][0] - lst[i][0]) + abs(lst[curr][1] - lst[i][1]) > 1000: continue
            v[i] = True
            q.append(i)
    print("happy" if v[len(lst)-1] else "sad")