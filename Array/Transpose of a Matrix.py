#Transpose of matrices
def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

# Example
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Transpose of the Matrix:")
for row in transpose_matrix(matrix):
    print(row)
