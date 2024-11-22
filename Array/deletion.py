def delete_element(arr, value):
    if value in arr:
        arr.remove(value)

# Example
arr = [10, 20, 30, 40, 50]
delete_element(arr, 30)
print("After deletion:", arr)
