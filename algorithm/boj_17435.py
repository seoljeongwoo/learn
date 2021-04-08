import sys
input = sys.stdin.readline
max_d = 19
m = int(input())
f = [0] + list(map(int,input().split()))
s_table = [[0]*19 for _ in range(m+1)]
for _ in range(1,m+1): s_table[_][0] = f[_]
for j in range(1,max_d):
    for i in range(1,m+1):
        s_table[i][j] = s_table[s_table[i][j-1]][j-1]
for _ in range(int(input())):
    n,x = map(int,input().split())
    for j in range(19):
        if n&1: x = s_table[x][j]
        n >>= 1
    print(x)