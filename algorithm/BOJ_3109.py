import sys
input = sys.stdin.readline
def dfs(x,y):
    visit[x][y] = True
    if y == M-1: return True

    for a,b in direction:
        nx ,ny = x+a,y+b
        if nx == -1 or nx == N or visit[nx][ny] == True or Bread[nx][ny] == 'x': continue

        if dfs(nx,ny) : return True
    return False
N,M= map(int,input().split())
Bread , direction = [] , [(-1,1), (0,1), (1,1)]
for _ in range(N):
    Bread.append(list(input().rstrip('\n')))

visit = [[False]*M for _ in range(N)]
result = 0

for i in range(N):
    if dfs(i,0): result+=1
print(result)

        
