def find_coins_greedy(amount):
    # Set of coin denominations
    coins = [50, 25, 10, 5, 2, 1]
    result = {}

    # Iterate over each coin denomination
    for coin in coins:
        if amount >= coin:
            count = amount // coin  # Calculate how many coins of this denomination are needed
            amount -= count * coin  # Subtract the total value of these coins from the amount
            result[coin] = count  # Store the count of this coin in the result dictionary

    return result
