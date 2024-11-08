# Given an m x n grid, find the number of unique paths from the top-left to the bottom-right cell, moving only down or right.

def uniquePaths(m, n):
    # Initialize a DP table with all 1s for the base cases
    dp = [[1] * n for _ in range(m)]
    
    # Fill the DP table using the recurrence relation
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    # The result is in the bottom-right corner
    return dp[m-1][n-1]
m1, n1 = 3, 7
print(uniquePaths(m1, n1))

m2, n2 = 3, 2
print(uniquePaths(m2, n2)) 