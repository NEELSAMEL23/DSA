def find_min(arr, n, k):
    min_sum = sum(arr[:k])  # Initialize min_sum with the sum of the first k elements
    current_sum = min_sum

    for i in range(k, n):  # Iterate from k to n
        current_sum = current_sum - arr[i - k] + arr[i]  # Update current_sum
        min_sum = min(min_sum, current_sum)  # Update min_sum if needed

    return min_sum

arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4
n = len(arr)  # Use the length of the array

res = find_min(arr, n, k)
print(res)  # This should print the minimum sum of any subarray of size k
