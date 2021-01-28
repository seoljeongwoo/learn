import sys
input = sys.stdin.readline
def f(u):
    if u!=p[u]:
        p[u]=f(p[u])
    return p[u]
def merge(u,v):
    u=f(u)
    v=f(v)
    if u==v:return
    p[u]=v
    return

N,M = int(input()), int(input())
p = [ _ for _ in range(N)]
for _ in range(N):
    for i,v in enumerate(list(map(int,input().split()))):
        if v: merge(_,i)
c = list(map(int,input().split()))
for i in range(1,M):
    if f(c[i-1]-1) != f(c[i]-1):
        print("NO")
        exit()
print("YES")