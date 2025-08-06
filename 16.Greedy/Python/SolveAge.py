def max_speed(n, arr):
    arr.sort()
    total = 0
    for i in range(0, 2*n, 2):
        total += arr[i]
    return total