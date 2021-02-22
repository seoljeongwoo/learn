import sys
input = sys.stdin.readline
N,M,K = map(int,input().split())
edge = [ [] for _ in range(N+1)]
rev_edge = [ [] for _ in range(N+1)]
inQ_state = [0]*(N+1)
build = [0] * (N+1)
for _ in range(M):
    u,v = map(int,input().split())
    edge[u].append(v)
    rev_edge[v].append(u)
    inQ_state[v] += 1
ok = True
for _ in range(K):
    x,y = map(int,input().split())
    if x == 1:
        if inQ_state[y] == 0: # build ok
            for __ in edge[y]:
                if inQ_state[__] > 0 : inQ_state[__] -=1
            build[y] += 1
        else:
            ok = False
            break
    else:
        if build[y] > 0 :   # delete ok
            build[y] -= 1
            if build[y] == 0:
                for __ in rev_edge[y]:
                    if inQ_state[__] == 0: continue
                    build[y] += 1
        else:
            ok = False
            break
print("King-God-Emperor" if ok else "Lier!")