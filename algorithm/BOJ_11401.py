import sys
input = sys.stdin.readline
N,K=map(int,input().split())
MOD = 1000000007
K = min(N-K,K)
num,inv=1,1
for i in range(1,K+1):
    num = num* (N-i+1)%MOD
    inv = inv * i % MOD
print(num*pow(inv,MOD-2,MOD)%MOD)