# Hardcoded input
n = 6
arr = [5, 2, 9, 1, 6, 3]

# Sort the array
arr.sort()

# Swap adjacent elements in pairs
for i in range(0, n - 1, 2):
    arr[i], arr[i + 1] = arr[i + 1], arr[i]

# Print the result
print(*arr)
