import sys
input = sys.stdin.readline

def find(u):
    if p[u] != u:
        p[u] = find(p[u])
    return p[u]
def merge(u,v):
    u = find(u)
    v = find(v)
    p[u] = v
    return
N,M=map(int,input().split())
T = 1
p = [i for i in range(N)]
for _ in range(M):
    A,B=map(int,input().split())
    if find(A) == find(B):
        print(T)
        exit()
    else:
        T+=1
        merge(A,B)
print(0)