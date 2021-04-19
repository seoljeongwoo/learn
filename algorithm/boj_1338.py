import sys
input = sys.stdin.readline

l,r = map(int,input().split())
if l>r : l,r = r,l
x,y = map(int,input().split())
if not (0<=y<abs(x)) : print("Unknwon Number");exit(0)
if x ==0 : 
    if l <= y <= r: print(y)
    else: print("Unknwon Number")
    exit(0)
l,r = l-y, r-y
if x<0:
    l,r = -1*r,-1*l
    new_x = -1*x
    lmok = l//new_x
    lna = l%new_x
    l = lmok +1 if lna !=0 else lmok
    r = r//new_x
    print(x*l+y if l==r else "Unknwon Number")
else:
    lmok = l//x
    lna = l%x
    l = lmok + 1 if lna !=0 else lmok
    r = r//x
    print(x*l+y if l==r else "Unknwon Number")
