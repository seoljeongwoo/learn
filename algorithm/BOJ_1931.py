import sys
input = sys.stdin.readline
N , h = int(input()) , []
for _ in range(N):
    a,b = map(int,input().split())
    h.append((b,a))
r,c=-1,0
h.sort()
for i in range(N):
    if h[i][1] < r: continue
    else: c+=1; r=h[i][0]
print(c)