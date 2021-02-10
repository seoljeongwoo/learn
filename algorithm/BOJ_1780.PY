import sys
input = sys.stdin.readline
N = int(input())
lst = [list(map(int,input().split())) for _ in range(N)]
def solve(x,y,size):
    if size == 1:
        if lst[x][y] == -1: return (1,0,0)
        elif lst[x][y] == 0: return (0,1,0)
        else: return (0,0,1)
    nsize = size//3
    direction = [(0,0),(0,nsize),(0,2*nsize),(nsize,0),(nsize,nsize),(nsize,2*nsize),(2*nsize,0),(2*nsize,nsize),(2*nsize,2*nsize)]
    MO,Z,O=0,0,0
    for a,b in direction:
        _MO,_Z,_O = solve(x+a,y+b,nsize)
        MO+=_MO;Z+=_Z;O+=_O
    if Z==0 and O==0: return (1,0,0)
    elif MO==0 and O==0: return (0,1,0)
    elif MO==0 and Z==0: return (0,0,1)
    else: return(MO,Z,O)
a,b,c = solve(0,0,N)
print(a)
print(b)
print(c)