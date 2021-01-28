st = set([])
def dfs(x,y,cnt,val):
    global st
    if cnt == 6:
        st.add(val)
        return
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if nx==-1 or nx==5 or ny==-1 or ny==5: continue
        dfs(nx,ny,cnt+1,val*10+lst[nx][ny])
    return
lst = [list(map(int,input().split())) for _ in range(5)]
dx,dy = [-1,0,1,0],[0,1,0,-1]
for i in range(5):
    for j in range(5):
        dfs(i,j,0,0)
print(len(st))