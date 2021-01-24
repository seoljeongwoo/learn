def cnt(sx,ex,sy,ey):
    W,B=0,0
    for i in range(sx,ex):
        for j in range(sy,ey):
            if i%2 == j%2:
                if lst[i][j] == 'W':
                    B+=1
                if lst[i][j] == 'B':
                    W+=1
            else:
                if lst[i][j] == 'W':
                    W+=1
                if lst[i][j] == 'B':
                    B+=1
    return min(W,B)

N,M=map(int,input().split())
lst = [list(input()) for _ in range(N)]
result = 2500
for i in range(N-7):
    for j in range(M-7):
        result = min(result,cnt(i,i+8,j,j+8))
print(result)