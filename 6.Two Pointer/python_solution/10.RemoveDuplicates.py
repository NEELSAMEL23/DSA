def RemoveDuplicates(arr):
    if not arr:
        return [], 0

    i = 1  # position to insert next allowed element
    count = 1  # count of current element occurrences

    for j in range(1, len(arr)):
        if arr[j] == arr[j - 1]:
            count += 1
        else:
            count = 1

        if count <= 2:
            arr[i] = arr[j]
            i += 1

    return arr[:i], i

arr = [1,1,1,1,3,3,3,3,4,6,6,6,6,6,6,7]
res, length = RemoveDuplicates(arr)
print(res)
print(length)
