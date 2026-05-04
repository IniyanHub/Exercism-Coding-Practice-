def find_fewest_coins(coins, target):
    if target < 0:
        raise ValueError("target can't be negative")

    # Initialize DP array
    dp = [float('inf')] * (target + 1)
    dp[0] = 0

    # To track which coin was used last
    prev = [-1] * (target + 1)

    for coin in coins:
        for amount in range(coin, target + 1):
            if dp[amount - coin] + 1 < dp[amount]:
                dp[amount] = dp[amount - coin] + 1
                prev[amount] = coin

    # If it's not possible to make the target
    if dp[target] == float('inf'):
        raise ValueError("can't make target with given coins")

    # Reconstruct the coins used
    result = []
    while target > 0:
        coin = prev[target]
        result.append(coin)
        target -= coin

    return sorted(result)
