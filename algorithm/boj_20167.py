import sys
input = sys.stdin.readline

def solve(curr, s):
    if curr == n:
        return max(s-k,0)
    ret = 0
    if s>=k:
        ret = max(solve(curr+1,0) , solve(curr+1, lst[curr])) + (s-k)
    else:
        ret = max(solve(curr+1,0) , solve(curr+1,s+lst[curr]))
    return ret
n,k= map(int,input().split())
lst = list(map(int,input().split()))
print(solve(0,0))