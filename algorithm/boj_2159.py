import sys
input = sys.stdin.readline

n = int(input())
sx,sy = map(int,input().split())
direction = [(-1,0), (1,0), (0,-1) , (0,1)]
ans = 0
xy = [(sx,sy)] * 5
dist = [0]*5
for _ in range(n):
    u,v = map(int,input().split())
    new_lst = [(u,v)] + list((u+dx,v+dy) for dx,dy in direction)
    new_dist = [int(1e12)+5]*5
    for i in range(5):
        px,py = xy[i]
        for j in range(5):
            cx,cy = new_lst[j]
            new_dist[j] = min(new_dist[j] , dist[i] + abs(px-cx) + abs(py-cy))
    xy , dist = new_lst, new_dist
print(min(dist))

