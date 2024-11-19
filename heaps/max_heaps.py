#A Max Heap is similar to a Min Heap, but the value of each node is greater than its children. Python’s heapq only supports Min Heap, so we can simulate a Max Heap using negative values.

import heapq

# Create a Max Heap
max_heap = []

# Insert elements into the heap (using negative values)
heapq.heappush(max_heap, -10)
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -20)

print("Max Heap:", [-x for x in max_heap])  # Convert back to positive values for display

# Extract the maximum element
max_element = -heapq.heappop(max_heap)
print("Extracted Max:", max_element)
print("Heap after extraction:", [-x for x in max_heap])
