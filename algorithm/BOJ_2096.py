import sys
input = sys.stdin.readline
N = int(input())
Max_DP = list(map(int,input().split()))
Min_DP = []
for d in Max_DP:
    Min_DP.append(d)
for _ in range(N-1):
    a,b,c = map(int,input().split())
    Max_DP[0],Max_DP[1],Max_DP[2] = max(Max_DP[0],Max_DP[1])+a,max(Max_DP[0],Max_DP[1],Max_DP[2])+b,max(Max_DP[1],Max_DP[2])+c
    Min_DP[0],Min_DP[1],Min_DP[2] = min(Min_DP[0],Min_DP[1])+a,min(Min_DP[0],Min_DP[1],Min_DP[2])+b,min(Min_DP[1],Min_DP[2])+c
print( max(Max_DP) , min(Min_DP))