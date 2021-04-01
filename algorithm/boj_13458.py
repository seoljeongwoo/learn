import sys
input = sys.stdin.readline

n = int(input())
lst = map(int,input().split())
b,c = map(int,input().split())
ret = 0 
for x in lst:
    if x > b:
        ret += (x-b)//c
        ret += 0 if (x-b)%c ==0 else 1
    ret += 1
print(ret)