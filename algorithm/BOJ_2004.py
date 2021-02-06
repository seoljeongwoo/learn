import sys
input = sys.stdin.readline
n,m = map(int,input().split())
Count5, Count2 =0, 0
i=1
while True:
    if n < 5**i: break
    Count5 += (n//(5**i))
    Count5 -= (m//(5**i))
    Count5 -= ((n-m)//(5**i))
    i+=1
i=1
while True:
    if n < 2**i: break
    Count2 += (n//(2**i))
    Count2 -= (m//(2**i))
    Count2 -= ((n-m)//(2**i))
    i+=1
print(min(Count5, Count2))