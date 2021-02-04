import sys
input = sys.stdin.readline
input()
lst = sorted(list(map(int,input().split())))
for _ in range(1,len(lst)):
    lst[_] += lst[_-1]
print(sum(lst))
