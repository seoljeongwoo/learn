import sys
input = sys.stdin.readline

N , dist , cost = int(input()), list(map(int,input().split())) , list(map(int,input().split()))
pre_dist, curr_cost = dist[0] , cost[0]
result = 0
for i in range(1,N-1):
    if curr_cost > cost[i]:
        result += (curr_cost) * pre_dist
        curr_cost = cost[i]
        pre_dist = dist[i]
    else:
        pre_dist += dist[i]
result += (curr_cost) * pre_dist
print(result)