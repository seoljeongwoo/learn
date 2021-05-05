import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))
for _ in range(1,n):
    lst[0] ^= lst[_]

if lst[0] == 0 : print("cubelover")
else: print("koosaga")
