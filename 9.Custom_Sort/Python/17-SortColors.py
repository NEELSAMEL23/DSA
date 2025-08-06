def solve(n, arr):
    low, mid, high = 0, 0, n - 1
    
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
            
    return arr  # Return sorted array

arr = [2, 0, 2, 1, 1, 0]
n = 6
res = solve(n, arr)
print(res)  # [0, 0, 1, 1, 2, 2]
# Dutch National Flag algorithm