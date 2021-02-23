import sys
from collections import deque
input = sys.stdin.readline

def shark_location():
    for i in range(N):
        for j in range(N):
            if state[i][j] == 9:
                state[i][j] = 0
                return (i,j)

def bfs(x,y,size):
    visit = [ [-1]*N for _ in range(N)]
    Q = deque()
    Q.append((x,y))
    min_dist = 401
    visit[x][y] = 0
    _next = (N,N)
    while Q:
        cx,cy = Q.popleft()

        if state[cx][cy] !=0 and state[cx][cy] < size:
            if min_dist >= visit[cx][cy]:
                _next = min(_next, (cx,cy))
                min_dist = min(min_dist, visit[cx][cy])

        for dx, dy in direction:
            nx,ny = cx+dx, cy+dy
            if nx == -1 or nx == N or ny == -1 or ny == N: continue
            if visit[nx][ny] != -1 or state[nx][ny] > size: continue
            visit[nx][ny] = visit[cx][cy] +1
            Q.append((nx,ny))
    if min_dist == 401:
        return -1, -1,-1
    else: return min_dist, _next[0],_next[1]

def eat():

    shark_x,shark_y=shark_location()
    shark_size , curr_eat, curr_time= 2, 0 , 0
    
    while True:
        next_dist, nextx, nexty = bfs(shark_x,shark_y,shark_size)
        if next_dist == -1: return curr_time
        curr_time += next_dist
        curr_eat += 1
        if shark_size == curr_eat:
            shark_size += 1
            curr_eat = 0
        state[nextx][nexty] = 0
        shark_x,shark_y = nextx, nexty

N = int(input())
state = [ list(map(int,input().split())) for _ in range(N)]
direction = [(-1,0), (1,0), (0,1) , (0,-1)]
print(eat())