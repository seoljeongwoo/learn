import sys
input = sys.stdin.readline
def BOJ_1992(x,y,size):
    if size == 0 : return
    
    cnt = 0
    for i in range(x,x+size):
        cnt += sum(lst[i][y:y+size])
    if cnt == 0:
        print(0,end="")
    elif cnt == size*size:
        print(1,end="")
    else:
        print('(',end="")
        BOJ_1992(x,y,size//2)
        BOJ_1992(x,y+size//2,size//2)
        BOJ_1992(x+size//2,y,size//2)
        BOJ_1992(x+size//2,y+size//2,size//2)
        print(')',end="")
    return

N= int(input())
lst = [ list(map(int,list(input().rstrip('\n')))) for _ in range(N)]
BOJ_1992(0,0,N)