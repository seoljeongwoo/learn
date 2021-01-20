import sys
input =sys.stdin.readline
TC = int(input())

for _ in range(TC):
    K = int(input())
    F = [0] + list(map(int,input().split()))
    DP = [[0]*(K+1) for _ in range(K+1)]
    Presum = [0] * (K+1)
    for i in range(1,K+1):
        Presum[i] = Presum[i-1] + F[i]
    for i in range(2,K+1):
        for j in range(1,K+2-i):
            DP[j][j+i-1] = min(DP[j][j+k] + DP[j+k+1][j+i-1] + Presum[j+i-1] - Presum[j-1] for k in range(i-1))
    print(DP[1][K])
