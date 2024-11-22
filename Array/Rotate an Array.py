def rotate_array(arr, k):
    k %= len(arr)  # Handle cases where k > len(arr)
    return arr[-k:] + arr[:-k]

# Example
arr = [1, 2, 3, 4, 5]
k = 2
print("Rotated array:", rotate_array(arr, k))
