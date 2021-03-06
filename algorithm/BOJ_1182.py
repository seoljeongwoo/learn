import sys
from itertools import combinations
input = sys.stdin.readline

cnt =0
n,s=map(int,input().split())
lst=list(map(int,input().split()))
for i in range(1,n+1):
    tmp = list(combinations(lst, i))
    for x in tmp:
        if sum(x)==s: cnt+=1
print(cnt)