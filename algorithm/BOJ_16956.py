import sys
input = sys.stdin.readline
direction = [(0,1),(0,-1),(1,0),(-1,0)]
R,C=map(int,input().split())
farm = []
for i in range(R):
    farm.append(list(input()))
wolfcheck = True
for i in range(R):
    for j in range(C):
        if farm[i][j] == 'W':
            for dx , dy  in direction:
                nx ,ny = i+dx,j+dy
                if 0<=nx <R and 0<=ny<C:
                    if farm[nx][ny] =='S':
                        wolfcheck = False
                    elif farm[nx][ny] == '.':
                        farm[nx][ny] = 'D'
if wolfcheck:
    print(1)
    for i in range(len(farm)):
        print(''.join(map(str,farm[i])))
else:
    print(0)

