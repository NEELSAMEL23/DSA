def binary_search_iterative(arr, k):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == k:
            return 1
        elif arr[mid] < k:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1


n, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

print(binary_search_iterative(arr, k))
