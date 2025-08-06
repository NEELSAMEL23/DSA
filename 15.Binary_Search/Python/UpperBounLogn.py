def upper_bound(arr, k):
    low, high = 0, len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] <= k:
            low = mid + 1
        else:
            high = mid
    return low

# Input reading
n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Find and print upper bound index
print(upper_bound(arr, k))
