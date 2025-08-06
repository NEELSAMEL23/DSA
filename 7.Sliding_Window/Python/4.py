# def subarray_sum_exist(arr,N,K):

#     for i in range(N):
#         sum = 0
#         for j in range(i,N):
#             sum += arr[j]
#             if sum == K:
#                 return True
#     return False

# arr = [1, 2, 3, 4, 5]
# N = 5
# K = 9

# res = subarray_sum_exist(arr,N,K)
# print(res)



def subarray_sum_exists(arr, N, K):
    current_sum = 0
    sum_map = {0: 1}  # Initialize with sum 0 to handle subarrays starting from index 0

    for num in arr:
        current_sum += num

        if current_sum - K in sum_map:
            return "Yes"

        if current_sum in sum_map:
            sum_map[current_sum] += 1
        else:
            sum_map[current_sum] = 1

    return "No"

arr = [1, 2, 3, 4, 5]
N = 5
K = 9

res = subarray_sum_exists(arr, N, K)
print(res)  # Output should be "Yes"




