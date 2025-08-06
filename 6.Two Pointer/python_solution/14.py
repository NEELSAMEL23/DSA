def merge_sorted_arrays(arr1, arr2):
    # Sort both arrays
    arr1.sort()
    arr2.sort()

    # Initialize pointers for both arrays
    i = 0
    j = 0
    merged_array = []

    # Merge the two arrays
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1

    # Append remaining elements of arr1
    while i < len(arr1):
        merged_array.append(arr1[i])
        i += 1

    # Append remaining elements of arr2
    while j < len(arr2):
        merged_array.append(arr2[j])
        j += 1

    return merged_array

arr1 = [1,2] 
arr2 = [3,2,1]
res = merge_sorted_arrays(arr1, arr2)
print(*res)