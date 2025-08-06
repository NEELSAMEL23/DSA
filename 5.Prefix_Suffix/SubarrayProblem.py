def count_even_sum_subarrays(arr):
    count = {0: 1, 1: 0} 
    prefix_sum = 0
    result = 0
    
    for num in arr:
        prefix_sum += num
        parity = prefix_sum % 2
        result += count[parity]
        count[parity] += 1
    
    return result


n = int(input())
arr = list(map(int, input().split()))
print(count_even_sum_subarrays(arr))
