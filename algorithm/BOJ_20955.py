import sys
input = sys.stdin.readline

def find(u):
    st = []
    while parent[u] != u:
        st.append(u)
        u = parent[u]
    while st:
        parent[st.pop()] = parent[u]
    return parent[u]

def merge(u,v):
    u = find(u)
    v = find(v)
    parent[u] = v
    return

N,M=map(int,input().split())
parent = [i for i in range(N+1)]
result = 0 
for _ in range(M):
    u,v = map(int,input().split())
    if find(u) == find(v) :
        result += 1
    else:
        merge(u,v)
st = set()
for _ in range(1,N+1):
    st.add(find(_))
print(result + len(st) -1)