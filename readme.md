1. **Greedy Algorithm**: Chooses the largest possible denomination first and proceeds until the total amount is reached.
2. **Dynamic Programming Algorithm**: Finds the minimum number of coins needed to reach the exact amount using dynamic programming.

## Results

### Greedy Algorithm
The Greedy algorithm is very fast. It works best with coin sets where each larger denomination is a multiple of the smaller denominations, such as [50, 25, 10, 5, 2, 1]. In these cases, it produces the same result as the Dynamic Programming algorithm. However, with other sets of coin denominations, it may not always provide the optimal solution.

### Dynamic Programming Algorithm
The Dynamic Programming algorithm guarantees finding the minimum number of coins for any coin set. It may take slightly longer to execute than the Greedy algorithm because it performs more calculations to ensure the optimal solution.

### Performance Comparison

- **Time Complexity:**
    - Greedy Algorithm: O(n), where n is the number of coin denominations.
    - Dynamic Programming: O(m*n), where m is the amount and n is the number of coin denominations.

- **Execution Time:**
    - The provided code measures execution time for both algorithms. The Greedy algorithm is usually faster, especially for large amounts. However, with the given coin set [50, 25, 10, 5, 2, 1], both algorithms produce the same result.

## Conclusion
The Greedy algorithm is effective and faster for coin sets where denominations are multiples of each other. For other coin sets, the Dynamic Programming algorithm should be used to ensure the minimum number of coins is given as change.