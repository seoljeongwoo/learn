import sys
input = sys.stdin.readline
MO,Z,O=0,0,0
def BOJ_1780(x,y,size):
    global MO,Z,O
    if size == 0: return
    mo,z,o= _lst[x+size+1][y+size+1] - _lst[x][y+size+1] - _lst[x+size+1][y] +_lst[x][y]
    if z==0 and o==0: MO+=1
    elif mo==0 and o==0: Z+=1
    elif mo==0 and z==0: O+=1
    else:
        nsize = size//3
        direction = [(0,0),(0,nsize),(0,nsize*2),(nsize,0),(nsize,nsize),(nsize,nsize*2),(nsize*2,0),(nsize*2,nsize),(nsize*2,nsize*2)]
        for a,b in direction:
            BOJ_1780(x+a,y+b,nsize)
    return

N = int(input())
lst = [list(map(int,input().split())) for _ in range(N)]
_lst = [(0,0,0)*(N+1) for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(1,N+1):
        for k in range(3):
            _lst[i][j][k] = _lst[i-1][j][k] + _lst[i][j-1][k] -_lst[i-1][j-1][k]
        if lst[i-1][j-1] == -1: _lst[i][j][0] +=1
        elif lst[i-1][j-1] == 0: _lst[i][j][1] +=1
        else : _lst[i][j][2] += 1

BOJ_1780(0,0,N)
print(MO)
print(Z)
print(O)