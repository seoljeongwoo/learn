import sys
def solve(x):
    dist = [10**6] * (x+1)
    path = [0]*(x+1)
    dist[1] ,path[1] = 0, 1
    for i in range(1, x+1):
        if i+1 <= x and dist[i+1] > dist[i]: dist[i+1], path[i+1] = dist[i] + 1 , i
        if 2*i <= x and dist[2*i] > dist[i]: dist[2*i], path[2*i] = dist[i] + 1 , i
        if 3*i <= x and dist[3*i] > dist[i]: dist[3*i], path[3*i] = dist[i] + 1 , i

    print(dist[x])
    path_result = []
    while path[x] != x:
        path_result.append(x)
        x = path[x]
    path_result.append(x)
    print(*path_result)
    return

x = int(input())
solve(x)

