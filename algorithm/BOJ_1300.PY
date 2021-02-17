import sys
input = sys.stdin.readline
N = int(input())
K = int(input())
lo ,hi = 0, N*N
while lo<=hi:
    mid = (lo+hi)//2

    cnt = 0
    for _ in range(1,N+1):
        cnt += min(N,mid//_)
    
    if cnt >= K:
        hi = mid-1
    else:
        lo = mid+1
print(lo)