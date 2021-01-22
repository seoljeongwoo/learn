import copy
import sys
input =sys.stdin.readline
N,M,K=map(int,input().split())
lst = [list(map(int,input().split())) for _ in range(N)]
op = list(map(int,input().split()))
def rotate(x):
    global N, M , lst
    if x == 1:  #상하 반전
        lst = lst[::-1]
    elif x == 2:    #좌우 반전
        lst = [row[::-1] for row in lst]
    elif x == 3:    # R90
        temp = [[0]*N for _ in range(M)]
        for i in range(M):
            for j in range(N):
                temp[i][j] = lst[N-j-1][i]
        lst = temp
        N,M = M,N
    elif x == 4:    # L90
        temp = [[0]*N for _ in range(M)]
        for i in range(M):
            for j in range(N):
                temp[i][j] = lst[j][M-1-i]
        lst = temp
        N,M=M,N
    elif x == 5:    # 2^N-1 R90
        temp = copy.deepcopy(lst)
        for i in range(0,N//2):
            for j in range(0,M//2):
                lst[i][j+M//2] = temp[i][j]
        for i in range(0, N//2):
            for j in range(M//2,M):
                lst[i+N//2][j] = temp[i][j]
        for i in range(N//2, N):
            for j in range(0,M//2):
                lst[i-N//2][j] = temp[i][j]
        for i in range(N//2,N):
            for j in range(M//2,M):
                lst[i][j-M//2] = temp[i][j]
    elif x== 6:     # 2^N-1 L90
        temp = copy.deepcopy(lst)
        for i in range(0,N//2):
            for j in range(0,M//2):
                lst[i+N//2][j] = temp[i][j]
        for i in range(0,N//2):
            for j in range(M//2,M):
                lst[i][j-M//2] = temp[i][j]
        for i in range(N//2,N):
            for j in range(0,M//2):
                lst[i][j+M//2] = temp[i][j]
        for i in range(N//2,N):
            for j in range(M//2,M):
                lst[i-N//2][j] = temp[i][j]
    return

for x in op:
    rotate(x)
for x in lst:
    print(*x)