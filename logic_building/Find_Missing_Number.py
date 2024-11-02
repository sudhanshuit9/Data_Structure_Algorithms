#Given an array containing n distinct numbers in the range [0, n], find the missing number.
def find_missing_number(nums):
    n = len(nums)
    
    expected_sum = n * (n + 1) // 2
   
    actual_sum = sum(nums)
    
    return expected_sum - actual_sum

nums = [3, 0, 1]
print("Missing number:", find_missing_number(nums))  
