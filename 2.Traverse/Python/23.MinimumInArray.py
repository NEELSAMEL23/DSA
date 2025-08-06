def min_value(arr, N):
    min_val = arr[0]
    for i in range(1, N):
        if arr[i] < min_val:
            min_val = arr[i]
    return min_val

arr = [1, 2, 3, 4, 5]
N = 5
print(min_value(arr, N))  # Output: 1
