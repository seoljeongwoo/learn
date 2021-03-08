import sys
input = sys.stdin.readline
n,m=map(int,input().split())
b=[list(input().rstrip('\n')) for _ in range(n)]
ar=dict()
jx,jy=-1,-1
for i in range(n):
    for j in range(m):
        if b[i][j]=='I':jx,jy=i,j;b[i][j]='.'
        elif b[i][j]=='R': ar[(i,j)]=1;b[i][j]='.'
direction=[(0,0),(1,-1),(1,0),(1,1),(0,-1),(0,0),(0,1),(-1,-1),(-1,0),(-1,1)]
order=list(input().rstrip('\n'))
for _ in range(len(order)):
    order[_] = ord(order[_])-ord('0')
for index,val in enumerate(order):
    jx,jy=jx+direction[val][0],jy+direction[val][1] #종수위치
    if (jx,jy) in ar.keys():print("kraj {0}".format(index+1));exit(0)
    next_ar=dict()
    for i,j in ar.keys():
        ni,nj=i,j

        if ni>jx:ni-=1
        elif ni<jx:ni+=1

        if nj>jy:nj-=1
        elif nj<jy:nj+=1
        if ni==jx and nj==jy: print("kraj {0}".format(index+1));exit(0)
        if (ni,nj) in next_ar.keys():
            next_ar[(ni,nj)]+=1
        else: next_ar[(ni,nj)]=1
    ar = dict()
    for x,v in next_ar.items():
        if v==1: ar[x]=1
b[jx][jy]='I'
for i,j, in ar.keys():
    b[i][j]='R'
for x in b:
    print(''.join(map(str,x)))