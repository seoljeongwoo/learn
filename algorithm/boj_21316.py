import sys
input = sys.stdin.readline

edge = [ [] for _ in range(13)]
for _ in range(12):
    u,v = map(int,input().split())
    edge[u].append(v)
    edge[v].append(u)

for _ in range(1,13):
    if len(edge[_]) == 3:
        one = 0
        three = 0
        for nx in edge[_]:
            if len(edge[nx]) == 1: one +=1
            if len(edge[nx]) == 3: three +=1
        if one == 1 and three ==1:
            print(_)
            exit(0)