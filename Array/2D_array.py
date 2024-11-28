#sum of the matrices
def add_matrices(matrix1, matrix2):
    rows, cols = len(matrix1), len(matrix1[0])
    result = [[matrix1[i][j] + matrix2[i][j] for j in range(cols)] for i in range(rows)]
    return result

# Example
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
print("Matrix Addition Result:")
for row in add_matrices(matrix1, matrix2):
    print(row)
