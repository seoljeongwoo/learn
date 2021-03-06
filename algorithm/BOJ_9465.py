import sys
input = sys.stdin.readline
T =int(input())
for _ in range(T):
    n = int(input())
    lst = [list(map(int,input().split())) for _ in range(2)]
    u,d,no = 0,0,0
    for i in range(n):
        u,d,no = max(d,no)+lst[0][i],max(u,no)+lst[1][i],max(u,d)
    print(max(u,d,no))