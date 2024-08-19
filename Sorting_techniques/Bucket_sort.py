def bucket_sort(arr):
    bucket = []
    for i in range(len(arr)):
        bucket.append([])

    for j in arr:
        index = int(10 * j)
        bucket[index].append(j)

    for i in range(len(arr)):
        bucket[i] = sorted(bucket[i])

    k = 0
    for i in range(len(arr)):
        for j in range(len(bucket[i])):
            arr[k] = bucket[i][j]
            k += 1
    return arr

arr = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51]
print(bucket_sort(arr))
