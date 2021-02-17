import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def solve(node , state):
    if DP[node][state] != -1: return DP[node][state]
    DP[node][state] = state
    visit[node] = True
    if state == 0:  # curr is not early
        for next_node in edge[node]:
            if visit[next_node] == True: continue
            DP[node][state] += solve(next_node, 1)
    else:   # curr is early
        for next_node in edge[node]:
            if visit[next_node] == True: continue
            DP[node][state] += min(solve(next_node,0) , solve(next_node,1))
    visit[node] = False
    return DP[node][state]

N = int(input())
DP = [[-1]*2 for _ in range(N+1)]
edge = [ [] for _ in range(N+1)]
visit = [False] * (N+1)
for _ in range(N-1):
    u,v=map(int,input().split())
    edge[u].append(v)
    edge[v].append(u)

print(min(solve(1,0) , solve(1,1)))


