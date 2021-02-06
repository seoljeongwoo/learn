import sys
input = sys.stdin.readline
N = int(input())
Count5 = 0
for i in range(2,N+1):
    if i%5 !=0 : continue
    num = i
    while num%5 == 0:
        Count5 += 1
        num//=5
print(Count5)