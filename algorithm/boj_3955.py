import sys
input = sys.stdin.readline

def crt(a,b):
    x,y,r1,r2,s1,s2=a,b,1,0,0,1
    while y!=0:
        mok = x//y
        na = x - (y*mok)
        x ,y = y,na
        r1,r2 = r2,r1-r2*mok
        s1,s2 = s2,s1-s2*mok
    if x != -1: print("IMPOSSIBLE")
    else:
        while r1 >0:
            r1 +=b
        if -r1 > int(1e9): print("IMPOSSIBLE")
        else: print(-r1)
    return 
t = int(input())
for _ in range(t):
    k,c = map(int,input().split())
    crt(c,-k)