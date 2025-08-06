def number_of_ways(n):
    dp = [0] * (n + 1)
    dp[0] = 1  
    for i in range(1, n + 1):
        dp[i] += dp[i - 1] if i - 1 >= 0 else 0
        dp[i] += dp[i - 2] if i - 2 >= 0 else 0
        dp[i] += dp[i - 3] if i - 3 >= 0 else 0
    return dp[n]

n = int(input())
print(number_of_ways(n))
