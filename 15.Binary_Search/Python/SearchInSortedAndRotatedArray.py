def search_rotated_array(arr, k):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == k:
            return mid

        # Left half is sorted
        if arr[low] <= arr[mid]:
            if arr[low] <= k < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        # Right half is sorted
        else:
            if arr[mid] < k <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1

# Input
n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Output
print(search_rotated_array(arr, k))
