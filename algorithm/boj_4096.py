import sys
sys.setrecursionlimit(202020)
input = sys.stdin.readline
def dfs(c):
    v[c] = True
    for n in edge[c]:
        if v[n]==True: continue
        dfs(n)
    st.append(c)
    return
def rev_dfs(c):
    v[c] = True
    for n in edge[c]:
        if v[n] == True: continue
        rev_dfs(n)
    return
t = int(input())
for _ in range(t):
    n,m=map(int,input().split())
    edge = [ [] for _ in range(n+1)]
    for __ in range(m):
        u,v = map(int,input().split())
        edge[u].append(v)
    st = []
    v = [False]*(n+1)
    for __ in range(1,n+1):
        if v[__] == False: dfs(__)
    ret = 0
    v = [False]*(n+1)
    while st:
        top = st.pop()
        if v[top] == True: continue
        rev_dfs(top)
        ret+=1
    print(ret)