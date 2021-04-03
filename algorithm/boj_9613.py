import sys
input = sys.stdin.readline
def gcd(a,b):
    return a if b==0 else gcd(b,a%b)
t =int(input())
for _ in range(t):
    lst = list(map(int,input().split()))
    ret = 0
    for i in range(1,lst[0]+1):
        for j in range(i+1,lst[0]+1):
            ret += gcd(lst[i], lst[j])
    print(ret)