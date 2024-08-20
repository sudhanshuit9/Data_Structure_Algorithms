#Binary search technique is basically used on the soeted array.
# AndBy dividing the search and interval of half repeatidly.

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [1, 2, 3, 4, 5, 6, 7]
target = 5
print(binary_search(arr, target))



#input  :1, 2, 3, 4, 5, 6, 7
#output : 4