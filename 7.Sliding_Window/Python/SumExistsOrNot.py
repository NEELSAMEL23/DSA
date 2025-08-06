def subset_sum_exists(arr, target):
    n = len(arr)
    for mask in range(1 << n):  # from 0 to 2^n - 1
        current_sum = 0
        for i in range(n):
            if mask & (1 << i):
                current_sum += arr[i]
        if current_sum == target:
            return "yes"
    return "no"

# Input
n = int(input())
arr = list(map(int, input().split()))
target = int(input())

# Output
print(subset_sum_exists(arr, target))
