def lower_bound(arr, k):
    low, high = 0, len(arr)
    result = -1
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < k:
            low = mid + 1
        else:
            high = mid
    if low < len(arr) and arr[low] == k:
        return low
    else:
        return -1

# Input reading
n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Print lower bound
print(lower_bound(arr, k))
