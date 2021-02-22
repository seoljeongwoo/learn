import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    a,b,c,d,e,f = map(int,input().split())
    if (c-d)*(e-f) < c*e: print("GOD")
    else: print("KDH")
        