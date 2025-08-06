def longest_subarray_with_sum_leq_k(arr, k):
    left = 0
    curr_sum = 0
    max_len = 0

    for right in range(len(arr)):
        curr_sum += arr[right]

        while curr_sum > k:
            curr_sum -= arr[left]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    print(longest_subarray_with_sum_leq_k(arr, K))
