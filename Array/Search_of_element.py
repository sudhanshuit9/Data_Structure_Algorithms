#Search an Element in 2D Array










def search_element(matrix, target):
    for i, row in enumerate(matrix):
        if target in row:
            return i, row.index(target)
    return -1, -1

# Example
matrix = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
target = 50
row, col = search_element(matrix, target)
if row != -1:
    print(f"Element found at Row: {row}, Column: {col}")
else:
    print("Element not found")








