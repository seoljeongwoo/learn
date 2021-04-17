import sys
input = sys.stdin.readline

def gcd(a,b):
    if b: return gcd(b,a%b)
    else : return a

N = int(input())
s = 0
ret = []
ms = 0
for _ in range(N):
    a,b = map(int,input().split())
    if a > 0:
        s += a
        if s != b:
            print(-1); exit(0)
    else:
        s += a
        if s >= 0:
            if s != b:
                print(-1); exit(0)
        else:
            ms = max(ms, b)
            ret.append(-1 * s + b)
            s = b
if len(ret) == 0: print(1)
elif len(ret) == 1:
    if 1<=ret[0] <= 9*(1e18) : print(ret[0])
    else: print(-1)
else:
    for j in range(1,len(ret)):
        ret[0] = gcd(ret[0] , ret[j])
        if ret[0] <= ms: print(-1); exit(0)
    if 1<= ret[0] <= 9*(1e18) :print(ret[0])
    else: print(-1)