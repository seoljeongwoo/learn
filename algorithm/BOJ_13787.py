import sys
input = sys.stdin.readline
direction = [(0,1),(1,0),(0,-1),(-1,0)]
while True:
    h,w,l= map(int,input().split())
    if h==0 and w==0 and l==0: break
    dic = dict()
    v = [[[40001 for col in range(w)] for row in range(h)] for depth in range(4)]
    m = [list(input().rstrip('\n')) for _ in range(h)]
    q = []
    for i in range(h):
        for j in range(w):
            if m[i][j] == 'E':
                v[0][i][j]=0
                q.append((i,j,0))
            elif m[i][j] == 'S':
                v[1][i][j]=0
                q.append((i,j,1))
            elif m[i][j] == 'W':
                v[2][i][j]=0
                q.append((i,j,2))
            elif m[i][j] == 'N':
                v[3][i][j]=0
                q.append((i,j,3))
    ok = True
    rx,ry,rd=-1,-1,-1
    while ok:
        x,y,d=q[-1]
        nd = d
        while True:
            nx,ny=x+direction[nd][0],y+direction[nd][1]
            if nx==-1 or nx==h or ny==-1 or ny==w or m[nx][ny]=='#': nd=(nd+1)%4; continue
            if v[nd][nx][ny] == 40001: 
                v[nd][nx][ny] = len(q); q.append((nx,ny,nd))
                if v[nd][nx][ny] == l: ok=False;rx,ry,rd=nx,ny,nd
                break
            st = v[nd][nx][ny]
            en = len(q)
            gap = en-st
            l -= st
            l = l%gap
            rx,ry,rd = q[st+l]
            ok=False
            break
    rx+=1;ry+=1
    if rd == 0:
        print(rx,ry,"E")
    elif rd==1:
        print(rx,ry,"S")
    elif rd==2:
        print(rx,ry,"W")
    else:
        print(rx,ry,"N")

        
