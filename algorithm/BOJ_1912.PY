#import sys
#input = sys.stdin.readline
N, lst= int(input()) , list(map(int,input().split()))
DP = [lst[0] for _ in range(N)]
for i in range(1,N):
    DP[i] = max(DP[i-1] + lst[i], lst[i])
print(max(DP))
