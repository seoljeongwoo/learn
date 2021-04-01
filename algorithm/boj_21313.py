import sys
input = sys.stdin.readline

n = int(input())
lst = [[False]*8 for _ in range(n)]
ret = []
for i in range(n):
    ok = 9
    for j in range(8):
        if lst[i][j] == False and lst[(i+1)%n][j] == False:
            ok = min(ok,j)
    ret.append(ok+1)
    lst[i][ok] = True
    lst[(i+1)%n][ok] = True
print(*ret)