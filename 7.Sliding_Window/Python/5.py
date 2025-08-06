def subarray_count_even_sum(arr,n):
    count = 0
    for i in range(n):
        current_sum  = 0
        for j in range(i,n):
            current_sum += arr[j]

            if current_sum %2==0:
                count += 1

    return count

arr = [ 2,5,4,4,4]
n = 5
res = subarray_count_even_sum(arr,n)
print(res)


def count_even_sum_subarrays(arr):
    even_count = 1  
    odd_count = 0
    prefix_sum = 0
    result = 0
    
    for num in arr:
        prefix_sum += num
        
        if prefix_sum % 2 == 0:
            result += even_count
            even_count += 1
        else:
            result += odd_count
            odd_count += 1
    
    return result

arr = [ 2,5,4,4,4]
n = 5
res = count_even_sum_subarrays(arr)
print(res)