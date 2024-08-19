# Brute force is the simplest approach where you try every possible outcomes solutions.

def find_max_brute_force(arr):
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

arr = [3, 1, 4, 1, 5, 9, 2, 6]
print(find_max_brute_force(arr))
