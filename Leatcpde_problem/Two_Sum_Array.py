# "Two Sum" problem using a dictionary (hash map) for efficient lookup:
# Input : nums = [2, 7,11,15], target =9
#Output : [0,1]

def two_sum(nums, target):
    num_map = {}  # Dictionary to store numbers and their indices
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []

# Example usage
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  # Output: [0, 1]


# This Approach runs in O(n) time complexity.