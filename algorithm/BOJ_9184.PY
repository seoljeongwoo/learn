import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
def boj_9184(x,y,z):
    if x<=0 or y<=0 or z<=0:
        return 1
    if DP[x][y][z] != -1:
        return DP[x][y][z]
    ret = 0 
    if x>20 or y>20 or z>20:
        ret = boj_9184(20,20,20)
    elif x<y<z:
        ret = boj_9184(x,y,z-1) + boj_9184(x,y-1,z-1) - boj_9184(x,y-1,z)
    else:
        ret = boj_9184(x-1,y,z) + boj_9184(x-1,y-1,z) + boj_9184(x-1,y,z-1) - boj_9184(x-1,y-1,z-1)
    DP[x][y][z] = ret
    return DP[x][y][z]

DP = [ [ [ -1 for i in range(51)]  for j in range(51)] for k in range(51)] 
while True:
    x,y,z = map(int,input().split())
    if x==-1 and y== -1 and z==-1:
        exit()
    print("w({0}, {1}, {2}) = {3}".format(x,y,z,boj_9184(x,y,z)))