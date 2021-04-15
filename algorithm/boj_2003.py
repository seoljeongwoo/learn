import sys
input = sys.stdin.readline

n,m = map(int,input().split())
a = list(map(int,input().split()))
left,right,s=0,0,0
ret = 0
while left < n and right <n :
    if s == m: ret += 1
    if s <=m : 
        s += a[right]
        right += 1
    else:
        s -= a[left]
        left += 1
while left < n:
    if s == m: ret += 1
    s -= a[left]
    left += 1
print(ret)
