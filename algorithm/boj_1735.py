import sys
input = sys.stdin.readline
def gcd(a,b):
    if b : return gcd(b,a%b)
    else: return a
a,b = map(int ,input().split())
c,d = map(int ,input().split())
ret1 = (a*d) + (b*c)
ret2 = b*d
print(ret1//gcd(ret1,ret2) , ret2//gcd(ret1,ret2))