def count_subarrays_less_than_m(arr, n, m):
    count = 0
    for start in range(n):
        current_sum = 0
        for end in range(start, n):
            current_sum += arr[end]
            if current_sum < m:
                count += 1
            else:
                break  # Stop early if the sum reaches or exceeds m
    return count

arr = [1,5,1,3,2]
n = 5
m = 5
res = count_subarrays_less_than_m(arr, n, m)
print(res)




def count_subarrays_less_than_m(arr, n, m):
    count = 0
    current_sum = 0
    start = 0
    
    for end in range(n):
        current_sum += arr[end]
        
        while current_sum >= m:
            current_sum -= arr[start]
            start += 1

        count += end - start + 1   
    return count

arr = [1,5,1,3,2]
n = 5
m = 5
res = count_subarrays_less_than_m(arr, n, m)
print(res)

