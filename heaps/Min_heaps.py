#A Min Heap is a binary tree where the value of each node is smaller than its children. It supports efficient minimum retrieval and insertion operations.
import heapq

# Create a Min Heap
min_heap = []

# Insert elements into the heap
heapq.heappush(min_heap, 10)
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 20)

print("Min Heap:", min_heap)

# Extract the minimum element
min_element = heapq.heappop(min_heap)
print("Extracted Min:", min_element)
print("Heap after extraction:", min_heap)
