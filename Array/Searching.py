#

def search_element(arr, value):
    if value in arr:
        return arr.index(value)
    return -1

# Example
arr = [10, 20, 30, 40, 50]
index = search_element(arr, 40)
print("Element found at index:" if index != -1 else "Element not found", index)
