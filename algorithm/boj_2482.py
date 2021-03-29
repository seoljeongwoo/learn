import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

def solve(curr, pick):
    
    if curr < 2*pick or curr==0: return 0
    if pick == 1: return curr

    if dp[curr][pick] != -1: return dp[curr][pick]
    dp[curr][pick] = (solve(curr-2,pick-1) + solve(curr-1,pick))%mod
    return dp[curr][pick]
    
n,k=int(input()), int(input())
mod = int(1e9)+3
dp = [[-1]*(n+1) for _ in range(n+1)]
print(solve(n,k))
