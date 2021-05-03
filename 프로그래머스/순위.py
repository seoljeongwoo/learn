def solution(n, results):
    answer = 0
    
    win = [ [] for _ in range(n+1)]
    lose = [ [] for _ in range(n+1)]
    
    for u,v in results:
        win[u].append(v)
        lose[v].append(u)
    
    
    for i in range(1,n+1):
        
        def dfs(curr, graph):
            vis[curr] = True
            ret = 0
            for nx in graph[curr]:
                if vis[nx] == True: continue
                ret += dfs(nx, graph)
            return ret + 1
        
        vis = [False] * (n+1)
        winner = dfs(i, win)
        vis = [False] * (n+1)
        loser = dfs(i,lose)
        
        if winner + loser - 2 == n-1: answer += 1

    return answer
