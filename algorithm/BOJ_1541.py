import sys
input = sys.stdin.readline
s = input()
minus = False
cx , result = -1, 0
while cx < len(s):
    nx = s.find('-',cx+1)
    ny = s.find('+',cx+1)
    
    if cx > -1 and s[cx] == '-': minus = True
    nnx = -1 
    if nx == -1 and ny == -1: nnx = -1
    elif nx!= -1 and ny == -1: nnx = nx
    elif nx ==-1 and ny != -1: nnx = ny
    else: nnx = min(nx,ny)

    if nnx == -1: break

    if minus == True: result -= int(s[cx+1:nnx])
    else : result += int(s[cx+1:nnx])
    cx = nnx
if minus == True: result -= int(s[cx+1:])
else : result += int(s[cx+1:])
print(result)