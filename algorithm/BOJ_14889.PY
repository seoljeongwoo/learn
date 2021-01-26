from itertools import combinations
import sys
input = sys.stdin.readline
def cal(a):
    s = 0 
    for i in range(len(a)):
        for j in range(len(a)):
            if i==j: continue
            s += stat[a[i]][a[j]]
    return s

N= int(input())
stat = [list(map(int,input().split())) for _ in range(N)]
c = list(combinations(map(str, range(N)),N//2))
r = int(1e9)
for i in range(len(c)//2):
    a,b = cal(list(map(int,c[i]))) , cal(list(map(int,c[-1-i])))
    r = min(r, abs(a-b))
print(r)