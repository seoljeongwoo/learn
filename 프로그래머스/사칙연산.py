def solution(arr):
    answer = 1
    SZ = len(arr)
    loop = (SZ+1)//2
    max_dp = [[-float('inf') for _ in range(SZ)] for __ in range(SZ)]
    min_dp = [[float('inf') for _ in range(SZ)] for __ in range(SZ)]
    
    for i in range(0,loop):
        max_dp[2*i][2*i] = min_dp[2*i][2*i] = int(arr[2*i])
    
    for gap in range(1,loop):
        for i in range(0,loop-gap):
            j = i+gap
            for k in range(i,j):

                if arr[2*k+1] == '+':
                    max_dp[2*i][2*j] = max(max_dp[2*i][2*j] , max_dp[2*i][2*k] + max_dp[2*(k+1)][2*j])
                    min_dp[2*i][2*j] = min(min_dp[2*i][2*j] , min_dp[2*i][2*k] + min_dp[2*(k+1)][2*j])
                else:
                    max_dp[2*i][2*j] = max(max_dp[2*i][2*j] , max_dp[2*i][2*k] - min_dp[2*(k+1)][2*j])
                    min_dp[2*i][2*j] = min(min_dp[2*i][2*j] , min_dp[2*i][2*k] - max_dp[2*(k+1)][2*j])

    answer = max_dp[0][SZ-1]
    return answer
