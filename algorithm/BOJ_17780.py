import sys
input = sys.stdin.readline
def check(check_x, check_y):
    return 0<=check_x<n and 0<=check_y<n

def White_process(num,cx,cy,nx,ny):
    for data in target_map[cx][cy]:
        target_map[nx][ny].append(data)
        target_x[data] = nx
        target_y[data] = ny
        target_is_bottom[data] = False
    target_map[cx][cy] = []
    target_is_bottom[target_map[nx][ny][0]] = True
    return True if len(target_map[nx][ny])>=4 else False

def Red_process(num,cx,cy,nx,ny):
    target_map[cx][cy].reverse()
    for data in target_map[cx][cy]:
        target_map[nx][ny].append(data)
        target_x[data] = nx
        target_y[data] = ny
        target_is_bottom[data] = False
    target_map[cx][cy] = []
    target_is_bottom[target_map[nx][ny][0]] = True
    return True if len(target_map[nx][ny]) >=4 else False

def Blue_process(num):
    cx,cy,cd = target_x[num], target_y[num], target_d[num]
    if cd %2 == 0: target_d[num] +=1; cd+=1
    else: target_d[num] -=1; cd-=1
    new_x,new_y = cx+direction[cd][0],cy+direction[cd][1]
    if not check(new_x,new_y) or map_color[new_x][new_y] == 2: return False
    elif map_color[new_x][new_y] ==0 : return White_process(num,cx,cy,new_x,new_y)
    else: return Red_process(num,cx,cy,new_x,new_y)
    
def solve():
    turn = 1
    while turn <=1000:
        for target_num in range(k):
            if not target_is_bottom[target_num]: continue
            x,y,d = target_x[target_num], target_y[target_num], target_d[target_num]
            nx,ny = x+direction[d][0] , y+direction[d][1]
            if not check(nx,ny) or map_color[nx][ny] == 2:    #Blue
                if Blue_process(target_num) : return turn
            elif map_color[nx][ny] == 0:
                if White_process(target_num,x,y,nx,ny) : return turn
            else:
                if Red_process(target_num,x,y,nx,ny) : return turn
        turn+=1
    return -1

n,k=map(int,input().split())
map_color = [ list(map(int,input().split())) for _ in range(n)]
direction = [(0,1) , (0,-1) , (-1,0), (1,0)]
target_map = [ [0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        target_map[i][j] = []
target_x, target_y, target_d = [0]*k, [0]*k, [0]*k
target_is_bottom = [True]*k
for target_num in range(k):
    x,y,d=map(int,input().split())
    target_map[x-1][y-1].append(target_num)
    target_x[target_num] = x-1
    target_y[target_num] = y-1
    target_d[target_num] = d-1
print(solve())
