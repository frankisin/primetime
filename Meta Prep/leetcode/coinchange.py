def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)

    dp[0] = 0 

    for a in range(1,amount+1):
        for coin in coins:
            if a - coin >= 0:
                dp[a] = min(dp[a],1+dp[a-coin])
    return dp[amount] if dp[amount] != float('inf') else -1 





   