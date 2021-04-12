import sys
input = sys.stdin.readline

def max_solve(n):
    ret = ""
    if n%2 == 0:
        ret += '1'*(n//2)
    else:
        ret += '7'
        n-=3
        ret += '1'*(n//2)
    return ret
def edge_plus():
    edge[2].append(1)
    edge[3].append(7)
    edge[4].append(4)
    edge[5].append(2)
    edge[6].append(0)
    edge[7].append(8)
    return

tc = int(input())
edge = [ [] for _ in range(8)]
edge_plus()
min_dp = [float('inf')]*101
for i in range(2,101):
    if i==6: min_dp[i] = 6
    elif i<=7: min_dp[i] = edge[i][0]
    else:
        for j in range(2,8):
            if i-j >=2:min_dp[i] = min(min_dp[i] , min_dp[i-j]*10 + edge[j][0])
    
for _ in range(tc):
    n = int(input())
    min_value = min_dp[n]
    max_value = max_solve(n)
    print(min_value , max_value)
