import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def robot(N , x, y , v):
    if N == 0 : return 1
    ret = 0
    for index,d in enumerate(direction) :
        nx , ny =  x+d[0] , y + d[1]
        if (nx,ny) in v.keys(): continue
        v[(nx,ny)] = True
        ret += robot(N-1, nx, ny, v) * per[index]/100
        del v[(nx,ny)]
    return ret

lst = input().rstrip().split()
direction = [( 0 , 1 ) , (0,-1) , (1,0) , (-1,0)]
N , per = int(lst[0]) , list(map(int ,lst[1:]))
dic = dict()
dic[(0,0)]= True
print(robot(N , 0, 0 , dic))
