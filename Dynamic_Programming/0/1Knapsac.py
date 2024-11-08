#Given weights and values of items and a knapsack capacity, find the maximum value achievable without exceeding the capacity.
def knapsack(values, weights, W):
    n = len(values)
    # Create a DP table with dimensions (n+1) x (W+1) initialized to 0
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    
    # Fill the DP table
    for i in range(1, n + 1):  # i represents items 1 to n
        for w in range(W + 1):  # w represents knapsack capacities 0 to W
            if weights[i - 1] <= w:
                # Item can be included, take the max of including or not including it
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][W]
