import time
from greedy_algorithm import find_coins_greedy
from dynamic_programming import find_min_coins

def main():
    amount = int(input("Enter the amount to give as change: "))

    # Using the Greedy algorithm
    start_time = time.time()
    greedy_result = find_coins_greedy(amount)
    greedy_time = time.time() - start_time
    print("Greedy algorithm result:")
    print(greedy_result)
    print(f"Execution time: {greedy_time:.6f} seconds\n")

    # Using the Dynamic Programming algorithm
    start_time = time.time()
    dp_result = find_min_coins(amount)
    dp_time = time.time() - start_time
    print("Dynamic programming result:")
    print(dp_result)
    print(f"Execution time: {dp_time:.6f} seconds")

if __name__ == "__main__":
    main()