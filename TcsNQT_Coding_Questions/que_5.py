#Implement Binary Search.
def binary_search_recursive(arr, left, right, target):
    if left > right:
        return -1  # Base case: not found

    mid = (left + right) 

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, mid + 1, right, target)  
    else:
        return binary_search_recursive(arr, left, mid - 1, target) 
    
#Test the function
arr = [2, 4, 6, 8, 10, 12]
target = 12
print(binary_search_recursive(arr, 0, len(arr) - 1, target)) 
  