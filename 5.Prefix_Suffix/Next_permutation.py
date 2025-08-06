def next_permutation(arr):
    n = len(arr)
    
    # Step 1: Find pivot
    i = n - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1

    if i >= 0:
        # Step 2: Find rightmost successor
        j = n - 1
        while arr[j] <= arr[i]:
            j -= 1
        # Step 3: Swap pivot and successor
        arr[i], arr[j] = arr[j], arr[i]

    # Step 4: Reverse suffix
    arr[i + 1:] = reversed(arr[i + 1:])
    return arr

# Hardcoded test case

arr =  [1, 2, 3]

res = next_permutation(arr)
print(res)