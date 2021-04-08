import sys
sys.setrecursionlimit(404040)
input = sys.stdin.readline
def q(left, right):
    ret = inf
    while left <right:
        if left%2 ==1 : ret = min(ret,seg[left]) ;left+=1
        if right%2 ==0 : ret = min(ret, seg[right]) ;right-=1
        left//=2; right//=2
    if left==right: ret = min(ret, seg[left])
    return ret
n,m = map(int,input().split())
lst = [int(input()) for _ in range(n)]
size = 1
while size < n:
    size <<= 1
inf = int(1e9)+1
seg=[inf]*(size*2)
for _ in range(n):
    seg[size+_] = lst[_]
for _ in range(size-1,0,-1):
    seg[_] = min(seg[_*2],seg[(_*2)+1])
for _ in range(m):
    a,b=map(int,input().split())
    a-=1; b-=1
    print(q(size+a,size+b))