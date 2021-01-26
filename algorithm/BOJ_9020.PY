import sys
input =sys.stdin.readline
def e():
    c[1] = False
    for i in range(2,int(N**0.5)+1):
        if c[i] == True:
            for j in range(i*i,N,i):
                c[j]=False
    return 
def gold(n):
    l=r=n//2
    while True:
        while c[l] != True: l-=1
        while c[r] != True: r+=1
        if l+r==n:
            return [l,r]
        elif l+r >n:
            l-=1
        else:
            r+=1
    return
N=10000
c=[True]*(N+1)
e()
T=int(input())
for _ in range(T):
    print(*(gold(int(input()))))
    