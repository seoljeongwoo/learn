##################################################
# kosaraju algorithm
# strongly connected component algorithm
# time complexity = O(n+m)
# 정방향 간선을 따라 dfs 순회를하면서 stack에 삽입
# (graph 를 트리 간선만으로 이루어진 dfs 트리를 만드는 과정)
# 트리 간선 : dfs 트리에 구성되어있는 간선
# stack의 Top 을 바탕으로 역방향 간선으로 dfs 수행
# 역방향 간선 : dfs 트리에서 자신의 부모노드로 돌아갈수있는 간선
# 역방향 dfs 수행중 도달할수있는 정점은 같은 scc
# 역방향 간선으로 도달할수 있는 정점은 cycle을 이루고 있다.
def kosaraju():

    def dfs(c):
        vis[c] = True
        for n in edge[c]:
            if not vis[n]:
                dfs(n)
        st.append(c)
        return
    def rev_dfs(c):
        vis[c] = True
        ret = [c]
        for n in rev_edge[c]:
            if not vis[n]:
                ret += rev_dfs(n)
        return ret

    v,e=map(int,input().split())
    edge = [ [] for _ in range(v+1)]
    rev_edge = [ [] for _ in range(v+1)]
    st = []
    for _ in range(e):
        a,b = map(int,input().split())
        edge[a].append(b)
        rev_edge[b].append(a)

    vis = [False] * (v+1)
    for i in range(1,v+1):
        if not vis[i]: dfs(i)
    vis = [False] * (v+1)
    scc = []
    while st:
        top = st.pop()
        if vis[top] : continue
        scc_lst = rev_dfs(top)
        scc_lst.sort()
        scc.append(scc_lst)
    scc.sort()
    print(len(scc))
    for data in scc:
        data.append(-1)
        print(*data)

#######################################

visit_cnt = -1
def targan():
    
    v,e=map(int,input().split())
    edge = [ [] for _ in range(v+1)]
    scc , st = [] , []
    visit , finish = [-1]*(v+1), [-1]*(v+1)
    def dfs(c):
        global visit_cnt
        visit_cnt += 1
        visit[c] = visit_cnt
        ret = visit[c]
        st.append(c)
        for n in edge[c]:
            if visit[n] == -1: ret = min(ret, dfs(n))
            elif finish[n] == -1: ret = min(ret, visit[n])
        if ret == visit[c]:
            scc_lst = []
            while st:
                top = st.pop()
                finish[top] = len(scc)
                scc_lst.append(top)
                if top == c: break
            scc_lst.sort()
            scc.append(scc_lst)
        return ret

    for _ in range(e):
        a,b=map(int,input().split())
        edge[a].append(b)
    for _ in range(1,v+1):
        if visit[_] == -1: dfs(_)
    scc.sort()
    print(len(scc))
    for data in scc:
        data.append(-1)
        print(*data)

