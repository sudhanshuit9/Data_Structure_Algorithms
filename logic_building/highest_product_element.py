#Given a list of integers, write a function that finds the two elements with the highest product.
def max_product_pair(nums):

    nums.sort(reverse=True)
    
   
    max_product_positive = nums[0] * nums[1]
    
   
    max_product_negative = nums[-1] * nums[-2]
    
    
    if max_product_positive > max_product_negative:
        return (nums[0], nums[1]), max_product_positive
    else:
        return (nums[-1], nums[-2]), max_product_negative


nums = [3, 6, -2, -5, 7, 3]
pair, max_product = max_product_pair(nums)
print("Pair with maximum product:", pair)
print("Maximum product:", max_product)  
