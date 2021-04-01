import sys
input = sys.stdin.readline

n = int(input())
lst = [0]+list(map(int,input().split()))
psum = [0]*(n+1)
for _ in range(1,n+1):
    if lst[_-1] > lst[_] : psum[_] = psum[_-1] + 1
    else: psum[_] = psum[_-1]
q = int(input())
for _ in range(q):
    x,y = map(int,input().split())
    print(psum[y] - psum[x])