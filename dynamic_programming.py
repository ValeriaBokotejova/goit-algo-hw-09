def find_min_coins(amount):
    # Set of coin denominations
    coins = [50, 25, 10, 5, 2, 1]
    # Initialize a DP array to store the minimum number of coins for each sum
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Base case: 0 coins needed for the amount 0
    result = {}

    # Calculate the minimum number of coins for each amount from 1 to the given amount
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # Backtrack to find the specific coins used
    while amount > 0:
        for coin in coins:
            if amount >= coin and dp[amount] == dp[amount - coin] + 1:
                result[coin] = result.get(coin, 0) + 1
                amount -= coin
                break

    return result
