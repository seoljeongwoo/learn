import sys
input =sys.stdin.readline

N,K = map(int,input().split())
coin , result= [] , 0
for _ in range(N):
    coin.append(int(input()))
for _ in range(N-1,-1,-1):
    result += (K//coin[_])
    K %= coin[_]
print(result)