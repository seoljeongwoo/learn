import sys
import bisect
input = sys.stdin.readline
T = int(input())
N = int(input())
A = [0] + list(map(int,input().split()))
M = int(input())
B = [0] + list(map(int,input().split()))
A_presum , B_presum = [], []
for i in range(1,N+1):
    A[i] += A[i-1]
for i in range(1,M+1):
    B[i] += B[i-1]
for i in range(1,N+1):
    for j in range(i,N+1):
        A_presum.append(A[j] - A[i-1])
for i in range(1,M+1):
    for j in range(i,M+1):
        B_presum.append(B[j] - B[i-1])
A_presum.sort()
B_presum.sort()
result = 0
for x in A_presum:
    left_idx = bisect.bisect_left(B_presum, T-x)
    right_idx = bisect.bisect_right(B_presum,T-x)
    result += (right_idx - left_idx)
print(result)