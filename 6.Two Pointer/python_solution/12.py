def Triple_Sum(arr, n):
    # Step 1: Sort the array
    arr.sort()

    # Step 2: Fix one element and use two pointers for the remaining two elements
    for k in range(n-1, 1, -1):  # Iterate over possible third elements
        i = 0
        j = k - 1

        while i < j:
            sum_pair = arr[i] + arr[j]
            if sum_pair == arr[k]:
                return 1  # Triplet found
            elif sum_pair < arr[k]:
                i += 1  # Increase the sum by moving left pointer to the right
            else:
                j -= 1  # Decrease the sum by moving right pointer to the left
    return 0  # No triplet found

# Test the function
arr = [7, 1, 2, 9, 4, 8, 6, 5]
n = len(arr)  # Length of the array
res = Triple_Sum(arr, n)
print(res)  # Output: 1
