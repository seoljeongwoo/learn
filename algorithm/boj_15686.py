import sys
from itertools import combinations
input = sys.stdin.readline

n,m = map(int,input().split())
house, retail =[], []
for i in range(n):
    lst = list(map(int,input().split()))
    for j,data in enumerate(lst):
        if data == 1: house.append((i,j))
        elif data ==2: retail.append((i,j))
lst = [i for i in range(len(retail))]
ret = int(1e9)
for data in list(combinations(lst,m)):
    dis = 0
    for i in range(len(house)):
        mindist = int(1e9)
        for j in data:
            mindist = min(mindist, abs(house[i][0] - retail[j][0]) + abs(house[i][1] - retail[j][1]))
        dis += mindist
    ret = min(ret, dis)
print(ret)
    

