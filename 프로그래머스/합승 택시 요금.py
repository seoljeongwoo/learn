def solution(n, s, a, b, fares):
    answer = float('inf')
    floyd = [ [ 0 if i == j else int(1e9) for i in range(n+1)] for j in range(n+1)]
    for u,v,cost in fares:
        floyd[u][v] = floyd[v][u] = cost
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if floyd[i][j] > floyd[i][k] + floyd[k][j]:
                    floyd[i][j] = floyd[i][k] + floyd[k][j]
    for i in range(1,n+1):
        answer = min(answer, floyd[s][i] + floyd[i][a] + floyd[i][b])
    return answer
