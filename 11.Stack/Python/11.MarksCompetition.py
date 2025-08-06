def find_greater_elements(arr,n):

    max_from_right = arr[-1]
    result = [max_from_right]
    
    for i in range(n-2, -1, -1):
        if arr[i] >= max_from_right:
            result.append(arr[i])
            max_from_right = arr[i]
    
    return result[::-1]  


n = 6
arr = [16,17,4,3,5,2]

res = find_greater_elements(arr,n)
print(*res)
