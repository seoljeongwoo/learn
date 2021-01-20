def ch(Alst , x, y):
    for i in range(x,x+3):
        for j in range(y,y+3):
            Alst[i][j] = 1-Alst[i][j]
    return Alst

N,M= map(int,input().split())
Alst = [list(map(int,list(input()))) for _ in range(N)]
Blst = [list(map(int,list(input()))) for _ in range(N)]

if N<3 or M<3:
    if Alst != Blst:
        print(-1)
    else:
        print(0)
    exit()

result = 0
for i in range(0,N-2):
    for j in range(0,M-2):
        if Alst[i][j] != Blst[i][j]:
            Alst = ch(Alst,i,j)
            result += 1
if Alst != Blst:
    print(-1)
else:
    print(result)