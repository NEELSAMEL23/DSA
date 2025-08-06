def max_subarray_sum(N, arr):
    max_sum = float('-inf')
    current_sum = 0

    for num in arr:
        current_sum += num
        max_sum = max(max_sum, current_sum)
        if current_sum < 0:
            current_sum = 0

    return max_sum

N = 5
arr = [1, 2, 0, 4, 5]
res = max_subarray_sum(N, arr)
print(res)