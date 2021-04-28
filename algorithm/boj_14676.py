import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
cnt = [0]*(n+1)
graph = [ [] for _ in range(n+1)]
ind = [0] *(n+1)
for _ in range(m):
    u,v=map(int,input().split())
    graph[u].append(v)
    ind[v] +=1

for _ in range(k):
    a,b = map(int,input().split())
    if a == 1:
        if ind[b] > 0:
            print("Lier!")
            exit(0)
        cnt[b] += 1
        for nx in graph[b]:
            ind[nx] -= 1
    else:
        if cnt[b] == 0:
            print("Lier!")
            exit(0)
        cnt[b] -= 1
        if cnt[b] == 0:
            for nx in graph[b]:
                ind[nx] += 1
print("King-God-Emperor")
