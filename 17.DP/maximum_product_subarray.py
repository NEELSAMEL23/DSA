def max_product_subarray(arr):
    max_prod = float('-inf')
    curr_max, curr_min = 1, 1  

    for num in arr:
        if num == 0:
            curr_max, curr_min = 1, 1
            max_prod = max(max_prod, 0)
            continue
        
        temp = curr_max * num
        curr_max = max(num, temp, curr_min * num)
        curr_min = min(num, temp, curr_min * num)
        
        max_prod = max(max_prod, curr_max)
    
    return max_prod

arr = [-3 ,0 ,-2]
res = max_product_subarray(arr)
print(res)