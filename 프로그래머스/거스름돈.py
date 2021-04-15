def solution(n, money):
    mod = int(1e9) + 7
    dp = [0]*(n+1)
    dp[0] = 1
    for value in money:
        for i in range(value, n+1):
            dp[i] = (dp[i] + dp[i-value])%mod
    answer = dp[n]
    return answer
