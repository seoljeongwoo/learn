import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline
def dfs(x,y,state,value):
    if state == 0:
        if Yes_RGB[x][y] == True: return
        Yes_RGB[x][y] = True

        for dx,dy in direction:
            nx,ny = x+dx, y+dy
            if nx == -1 or nx == N or ny == -1 or ny == N or RGB[nx][ny] != value or Yes_RGB[nx][ny] == True: continue
            dfs(nx,ny,state,value)
    else:
        if No_RGB[x][y] == True: return
        No_RGB[x][y] = True

        for dx, dy in direction:
            nx,ny = x+dx, y+dy
            if nx==-1 or nx == N or ny == -1 or ny ==N or No_RGB[nx][ny] == True: continue
            if value == 'B':
                if RGB[nx][ny] == 'B': dfs(nx,ny,state,value)
            else:
                if RGB[nx][ny] == 'R' or RGB[nx][ny] == 'G': dfs(nx,ny,state,value)
    return
N = int(input())
RGB = [ list(input().rstrip('\n')) for _ in range(N)]
Yes_RGB , No_RGB = [[False]*N for _ in range(N)] , [[False]*N for _ in range(N)]
Yes , No = 0 , 0
direction = [(-1,0) , (1,0) , (0,1) , (0,-1)]
for i in range(N):
    for j in range(N):
        if Yes_RGB[i][j] == False:
            dfs(i,j,0,RGB[i][j])
            Yes+=1
        if No_RGB[i][j] == False:
            dfs(i,j,1,RGB[i][j])
            No+=1
print(Yes, No)
        