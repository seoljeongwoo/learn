from itertools import permutations
import copy
import sys
input = sys.stdin.readline
N,M,K= map(int,input().split())
a , ro = [list(map(int,input().split())) for _ in range(N)], []
for _ in range(K):
    r,c,s = map(int,input().split())
    ro.append((r-1,c-1,s))
permut = list(permutations([i for i in range(K)],K))

def solve(temp, r,c,s):
    dx,dy = [0,1,0,-1], [1,0,-1,0]
    for i in range((2*s+1)//2):
        fx,fy,value = r-s+i,c-s+i,temp[r-s+i][c-s+i]
        d = 0
        while True:
            fx,fy = fx+dx[d] , fy+dy[d]
            if fx == r-s+i-1 or fx == r+s-i+1 or fy == c-s+i-1 or fy == c+s-i+1:
                fx,fy = fx-dx[d], fy-dy[d]
                d += 1
                fx,fy = fx+dx[d], fy+dy[d]
            if fx == r-s+i and fy == c-s+i:
                temp[fx][fy] = value
                break
            temp[fx][fy], value = value, temp[fx][fy]
    return temp
    

result = int(1e9)
for data in permut:
    temp = copy.deepcopy(a)
    for op in data:
        r,c,s = ro[op]
        temp = solve(temp , r, c, s)
    for data in temp:
        result = min(result , sum(data))
print(result)