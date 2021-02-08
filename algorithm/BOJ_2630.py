import sys
input = sys.stdin.readline
Z,O=0,0
def make(x,y,size):
    global Z,O
    if size == 0: return
    
    cnt = 0
    for i in range(x,x+size):
        cnt += sum(lst[i][y:y+size])

    if cnt == 0 : O+=1
    elif cnt == size*size: Z+=1
    else: 
        make(x,y,size//2)
        make(x,y+size//2,size//2)
        make(x+size//2,y,size//2)
        make(x+size//2,y+size//2,size//2)
    return
N = int(input())
lst =  [list(map(int,input().split())) for _ in range(N)]
make(0,0,N)
print(O)
print(Z)