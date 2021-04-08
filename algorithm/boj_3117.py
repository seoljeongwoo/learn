import sys
input = sys.stdin.readline

max_d = 31
n,k,m = map(int,input().split())
view = list(map(int,input().split()))
order = [0] + list(map(int,input().split()))
sp_table = [[0]*max_d for _ in range(k+1)]
for _ in range(1,k+1):
    sp_table[_][0] = order[_]
for j in range(1,max_d):
    for i in range(1,k+1):
        sp_table[i][j] = sp_table[sp_table[i][j-1]][j-1]
ret = []
for data in view:
    x = data
    t = m-1
    for bit in range(max_d):
        if t&1: x = sp_table[x][bit]
        t >>= 1
    ret.append(x)
print(*ret)

