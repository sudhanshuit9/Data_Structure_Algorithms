# Two pointer approach is commonly used for problems involving arrays. 
# Such as finding pairs of numbers that satisfy certain conditions.

def two_sum(arr, target):
    arr.sort()
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return (arr[left], arr[right])
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return None

arr = [2, 7, 11, 15]
target = 9
print(two_sum(arr, target))


