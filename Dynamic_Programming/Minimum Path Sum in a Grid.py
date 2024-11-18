def minPathSum(grid):
    m, n = len(grid), len(grid[0])
    
    # Initialize the DP array for the first row
    dp = [0] * n
    dp[0] = grid[0][0]
    
    # Fill the first row
    for j in range(1, n):
        dp[j] = dp[j-1] + grid[0][j]
    
    # Update the DP array for the remaining rows
    for i in range(1, m):
        dp[0] += grid[i][0]  # Update the first column
        for j in range(1, n):
            dp[j] = grid[i][j] + min(dp[j], dp[j-1])
    
    return dp[n-1]
