#
def update_element(arr, index, value):
    if 0 <= index < len(arr):
        arr[index] = value

# Example
arr = [10, 20, 30, 40, 50]
update_element(arr, 3, 45)
print("After updating:", arr)
