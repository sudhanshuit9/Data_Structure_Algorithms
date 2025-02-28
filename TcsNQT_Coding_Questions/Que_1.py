#Find the second Largest elements in the given array.
def second_Largest(arr):
    if len(arr) < 2:
        return None
    arr.sort()
    return arr[-2]

#Test the function
arr = [10,20,30,40,50]
print(second_Largest(arr))

