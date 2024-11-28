#1. Create and Traverse a 3D Array
def create_and_traverse_3d_array(depth, rows, cols):
    array_3d = [[[i * rows * cols + j * cols + k + 1 for k in range(cols)] for j in range(rows)] for i in range(depth)]
    for layer in array_3d:
        for row in layer:
            print(row)
        print()
    return array_3d

# Example
depth, rows, cols = 2, 3, 3
print("3D Array:")
create_and_traverse_3d_array(depth, rows, cols)
