import sys
from bisect import bisect_left
from bisect import bisect_right
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))
psum = [0]*n
for i in range(1,n):
    if lst[i-1] == lst[i]: psum[i] = psum[i-1]
    else: psum[i] = i

ret = []
for _ in range(n):
    p = lst[_] + psum[_]
    ok = True
    while True:
        l = bisect_left(lst, p)
        r = bisect_right(lst, p)
        if l==0 and r==n:
            ok=False; break
        if r == n: break
        if lst[l] > p: 
            ok=False; break
        else:
            p += (r-l)
    if ok: ret.append(_+1)
if len(ret) ==0: print(-1)
else: print(*ret)