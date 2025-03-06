#Find the first and last occurrence of an element in a sorted array.
def find_first_last_occurrence(arr, target):
    def find_first_occurrence(arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left if left < len(arr) and arr[left] == target else -1

    def find_last_occurrence(arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return right if right >= 0 and arr[right] == target else -1

    return find_first_occurrence(arr, target), find_last_occurrence(arr, target)




