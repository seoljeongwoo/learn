import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    w,h = map(int,input().split())
    lst.append((-1*(w**2+h**2),_))
lst.sort()
for value, index in lst:
    print(index+1)