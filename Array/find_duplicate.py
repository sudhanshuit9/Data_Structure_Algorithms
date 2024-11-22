def find_duplicates(arr):
    seen = set()
    duplicates = set()
    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)

# Example
arr = [1, 2, 3, 1, 2, 4]
print("Duplicate elements:", find_duplicates(arr))
