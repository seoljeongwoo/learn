import sys
from bisect import bisect_left

N , A = int(input()) , list(map(int,input().split()))
dp = [A[0]]
for i in range(1,len(A)):
    idx = bisect_left(dp, A[i])
    if len(dp) <= idx:
        dp.append(A[i])
    else:
        dp[idx] = A[i]
print(len(dp))