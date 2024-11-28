import numpy as np

def sum_across_dimensions(array):
    array_np = np.array(array)
    sum_depth = np.sum(array_np, axis=0)  # Sum across depth
    sum_rows = np.sum(array_np, axis=1)  # Sum across rows
    sum_cols = np.sum(array_np, axis=2)  # Sum across columns
    return sum_depth, sum_rows, sum_cols

# Example
array = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
]
depth_sum, row_sum, col_sum = sum_across_dimensions(array)
print("Sum Across Depth:\n", depth_sum)
print("Sum Across Rows:\n", row_sum)
print("Sum Across Columns:\n", col_sum)
