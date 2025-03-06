#Find if an array contains duplicate elements.
def has_duplicates(arr):
    return len(arr) != len(set(arr))
#Test the functions
print(has_duplicates([1,2,3,4,5]))

