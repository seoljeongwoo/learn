import sys
from collections import deque
input = sys.stdin.readline
fuel = -1
tx,ty=-1,-1
def check(x,y):
    return 0<=x<n and 0<=y<n
def solve():
    global fuel,tx,ty
    process_cnt = 0
    while process_cnt < m:
        v = [[-1]*n for _ in range(n)]
        q = deque()
        q.append((tx,ty))
        v[tx][ty] = 0
        while q:
            cx,cy = q.popleft()
            for dx,dy in direction:
                nx,ny = cx+dx,cy+dy
                if not check(nx,ny): continue
                if v[nx][ny] != -1 or lst[nx][ny] == 1: continue
                v[nx][ny] = v[cx][cy] + 1
                q.append((nx,ny))
        distance = int(1e9)
        pick_number = -1

        for i in range(m):
            if process[i] == True: continue
            if distance > v[customer[i][0]][customer[i][1]]:
                distance = v[customer[i][0]][customer[i][1]]
                pick_number = i
            elif distance == v[customer[i][0]][customer[i][1]]:
                tuple_first = (customer[pick_number][0] , customer[pick_number][1])
                tuple_second = (customer[i][0], customer[i][1])
                if tuple_first > tuple_second:
                    pick_number = i
        if distance == -1:
            fuel = -1; return
        v = [[-1]*n for _ in range(n)]
        q = deque()
        q.append((customer[pick_number][0], customer[pick_number][1]))
        v[customer[pick_number][0]][customer[pick_number][1]] = 0
        while q:
            cx,cy = q.popleft()
            for dx,dy in direction:
                nx,ny = cx+dx,cy+dy
                if not check(nx,ny): continue
                if v[nx][ny] != -1 or lst[nx][ny] == 1: continue
                v[nx][ny] = v[cx][cy] + 1
                q.append((nx,ny))
        dist = v[customer[pick_number][2]][customer[pick_number][3]]
        if dist == -1:
            fuel = -1; return
        if dist + distance > fuel:
            fuel = -1; return
        fuel = (fuel - dist - distance) + dist*2
        process[pick_number] = True
        process_cnt +=1
        tx,ty = customer[pick_number][2], customer[pick_number][3]
    return
        
n, m ,fuel = map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(n)]
tx,ty = map(int,input().split())
tx-=1;ty-=1
direction = [(-1,0),(1,0),(0,1),(0,-1)]
customer = []
process = [False]*m
for _ in range(m):
    sx,sy,desx,desy = map(int,input().split())
    sx-=1;sy-=1;desx-=1;desy-=1
    customer.append((sx,sy,desx,desy))
solve()
print(fuel)