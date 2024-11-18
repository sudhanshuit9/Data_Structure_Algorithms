# Given a rod of length n and prices of smaller pieces, determine the maximum obtainable profit by cutting up the rod and selling the pieces.

def cutRod(prices, n):
    # Create a DP array to store maximum profit for each length
    dp = [0] * (n + 1)
    
    # Loop through all rod lengths from 1 to n
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            dp[i] = max(dp[i], prices[j - 1] + dp[i - j])
    
    return dp[n]

prices1 = [2, 5, 9, 8]
n1 = 4
print(cutRod(prices1, n1))
