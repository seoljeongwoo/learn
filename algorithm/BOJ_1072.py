import sys
input = sys.stdin.readline

x,y = map(int ,input().split())
z = 100*y//x
if x==y or z==99: 
    print(-1)
    exit()

up = x*z+x-100*y
down = 99-z
if up % down == 0:
    print(up//down)
else:
    print(up//down + 1)
