# Sort an array using Merge Sort / Quick Sort.
def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)  
        quick_sort(arr, low, pivot_index - 1)   
        quick_sort(arr, pivot_index + 1, high)  

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  

    arr[i + 1], arr[high] = arr[high], arr[i + 1] 
    return i + 1  

# Example usage
arr = [8, 4, 7, 3, 9, 1]
quick_sort(arr, 0, len(arr) - 1)
print(arr)  # Output: [1, 3, 4, 7, 8, 9]





    


    
    