def find_min_in_rotated_sorted_array(arr):
    low, high = 0, len(arr) - 1

    while low < high:
        mid = (low + high) // 2

        if arr[mid] > arr[high]:
            low = mid + 1
        else:
            high = mid

    return arr[low]

# Input
n = int(input())
arr = list(map(int, input().split()))

# Output
print(find_min_in_rotated_sorted_array(arr))
