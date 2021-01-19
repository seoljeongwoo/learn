import sys
sys.setrecursionlimit(10**6)
def multi(A_dir, B_dir):
    tmp = [[0]*8 for _ in range(8)]
    for i in range(8):
        for j in range(8):
            for k in range(8):
                tmp[i][j] += A_dir[i][k] * B_dir[k][j]
    return tmp
def _pow(dir,D):
    if D==1:
        return dir
    new_dir = _pow(dir,D//2)
    new_dir = multi(new_dir,new_dir)
    
    if D%2 != 0:
        new_dir = multi(new_dir, dir)
    return new_dir

dir = [[0]*8 for _ in range(8)]
dir[0][1] ,dir[0][2] = 1,1
dir[1][0] , dir[1][2] , dir[1][3] = 1,1,1
dir[2][0] , dir[2][1] ,dir[2][3], dir[2][4] = 1,1,1,1
dir[3][1] , dir[3][2] , dir[3][4], dir[3][5] = 1,1,1,1
dir[4][2] , dir[4][3] , dir[4][5] ,dir[4][7]= 1,1,1,1
dir[5][3], dir[5][4] , dir[5][6] = 1,1,1
dir[6][5] , dir[6][7] = 1,1
dir[7][4] , dir[7][6] = 1,1

D = int(input())
dir = _pow(dir,D)
print(dir[0][0]%1000000007)