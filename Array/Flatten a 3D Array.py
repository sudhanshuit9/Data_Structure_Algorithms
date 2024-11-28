#Flater a 3D Array
def flatten_3d_array(array):
    return [elem for layer in array for row in layer for elem in row]

# Example
array = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
print("Flattened 3D Array:", flatten_3d_array(array))
