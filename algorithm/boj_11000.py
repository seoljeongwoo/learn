import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    a,b = map(int,input().split())
    lst.append((a,1))
    lst.append((b,-1))
lst.sort()
ret , s =0, 0
for a,b in lst:
    s += b
    ret = max(ret, s)
print(ret)

