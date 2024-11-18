# Given a set of positive integers, determine if it can be partitioned into two subsets with equal sums.

def canPartition(nums):
    total_sum = sum(nums)
    
    # If the total sum is odd, it's impossible to partition into two equal subsets
    if total_sum % 2 != 0:
        return False
    
    target = total_sum // 2
    dp = [False] * (target + 1)
    dp[0] = True  # We can always make a sum of 0 with an empty subset
    
    for num in nums:
        # Update dp array from right to left to ensure each num is only used once
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]
    
    return dp[target]

