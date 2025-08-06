def masai_numbers_game(arr):
    n = len(arr)
    result = [-1] * n
    
    
    f = [-1] * n
    
   
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] < arr[j]:
                f[i] = j
                break
    
    
    for i in range(n):
        if f[i] != -1:
            for j in range(f[i] + 1, n):
                if arr[f[i]] > arr[j]:
                    result[i] = arr[j]
                    break
        elif f[i] != -1:
            result[i] = arr[f[i]]
    
    return result


arr = [8,3,7,1,7,8,4,5,2]
res = masai_numbers_game(arr)
print(res)