import sys
input = sys.stdin.readline

a,b=list(input().rstrip('\n')),list(input().rstrip('\n'))
asize,bsize = len(a),len(b)
dp = [[0]*(bsize+1) for _ in range(asize+1)]
for i in range(1,asize+1):
    for j in range(1,bsize+1):
        if a[i-1] == b[j-1]: dp[i][j] = dp[i-1][j-1] + 1
        else: dp[i][j] = max(dp[i-1][j] , dp[i][j-1])
print(dp[asize][bsize])

result_print = []
while dp[asize][bsize] > 0:
    while dp[asize-1][bsize] == dp[asize][bsize]: asize-=1
    while dp[asize][bsize-1] == dp[asize][bsize]: bsize-=1
    result_print.append(a[asize-1])
    asize-=1; bsize-=1
result_print = result_print[::-1]
print(''.join(map(str,result_print)))