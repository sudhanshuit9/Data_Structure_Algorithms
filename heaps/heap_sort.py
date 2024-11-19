#Heap Sort uses a Min or Max Heap to sort an array. Here's how it works using a Min Heap:

import heapq

def heap_sort(arr):
    min_heap = []
    sorted_array = []

    # Build the Min Heap
    for element in arr:
        heapq.heappush(min_heap, element)

    # Extract elements in sorted order
    while min_heap:
        sorted_array.append(heapq.heappop(min_heap))

    return sorted_array

# Example
array = [20, 10, 30, 5, 50]
sorted_array = heap_sort(array)
print("Sorted Array:", sorted_array)
