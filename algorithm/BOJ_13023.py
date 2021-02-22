import sys
input = sys.stdin.readline
def dfs(curr,cnt):
    if cnt == 4: return True
    visit[curr] = True

    for _ in edge[curr]:
        if visit[_] == True: continue
        if dfs(_,cnt+1) == True: return True
    visit[curr] = False
    return False
    
N,M=map(int,input().rstrip('\n').split())
edge = [ [] for _ in range(N)]
for _ in range(M):
    u , v = map(int,input().rstrip('\n').split())
    edge[u].append(v)
    edge[v].append(u)
ok = False
for _ in range(N):
    visit = [False] * N
    if dfs(_,0) == True: ok= True
    if ok == True: break
if ok == True: print(1)
else: print(0)
