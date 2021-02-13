import sys
input = sys.stdin.readline
def DFS(curr):
    if visited[curr] == True: return
    visited[curr] = True

    for _next in edge[curr]:
        if visited[_next] == True: continue
        DFS(_next)
    return

N,M=map(int,input().split())
Truth = list(map(int,input().split()))
party = [ [0] for _ in range(M)]
edge = [ [] for _ in range(N+1)]
for i in range(M):
    lst = list(map(int,input().split()))
    if len(lst) == 1:  continue
    party[i] = list(lst[1:])
    for j in range(1,len(lst)):
        for k in range(j+1,len(lst)):
            edge[lst[j]].append(lst[k])
            edge[lst[k]].append(lst[j])
visited = [False] * (N+1)
for i in range(1,len(Truth)):
    DFS(Truth[i])
result = 0
for i in range(M):
    ok = True
    for x in party[i]:
        if visited[x] == True:
            ok = False
    if ok: result += 1
print(result)
