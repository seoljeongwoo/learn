import sys
input = sys.stdin.readline
n,m = map(int,input().split())
lst = [list(input().rstrip('\n')) for i in range(n)]
temp = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if j+1 <m and lst[i][j] != lst[i][j+1]:
            temp[i][j] = 1
            temp[i][j+1] = 1
        if i+1 < n and lst[i][j] != lst[i+1][j]:
            temp[i][j] = 1
            temp[i+1][j] = 1
cnt = 0 
for i in range(n):
    for j in range(m):
        if temp[i][j] == 1: cnt +=1
mod = int(1e9) + 7
print(pow(2,n*m-cnt,mod))