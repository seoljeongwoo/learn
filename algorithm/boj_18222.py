import sys
def solve(v):
    if v == 1: return 0
    elif v == 2: return 1
    a = 1
    while a < v: a*=2
    gap = a - v
    return 1-solve(a//2 - gap)
n = int(input())
print(solve(n))
