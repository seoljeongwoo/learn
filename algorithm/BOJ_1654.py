import sys
input = sys.stdin.readline
K,N=map(int,input().split())
LAN = []
for _ in range(K):
    LAN.append(int(input()))
lo , hi , result = 0 , (1<<31) , 1
while lo < hi:
    mid = (lo+hi)//2
    cnt = 0
    for i in LAN: cnt += (i//mid)
    
    if cnt >= N: 
        result = mid
        lo = mid+1
    else:
        hi = mid
print(result)