def even_array_sum(arr, N):
    sum = 0
    for i in range(N):
        if arr[i] % 2 == 0:
            sum += arr[i]
    return sum

# Hardcoded input
N = 5
arr = [1, 2, 3, 4, 5]
res = even_array_sum(arr, N)
print(res)
