import sys
input = sys.stdin.readline
N = int(input())
weight = list(map(int,input().split()))
edge = [ [] for _ in range(N+1)]
for _ in range(N-1):
    u,v = map(int,input().split())
    edge[u].append(v)
    edge[v].append(u)
visit = [False] * (N+1)
