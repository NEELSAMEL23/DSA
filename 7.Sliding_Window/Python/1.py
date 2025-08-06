def find_max(arr, n, k):

    max_sum = 0
    for i in range(1,n-k+2):
        current_sum = 0
        for j in range(i-1,i+k-1):
            current_sum += arr[j]

        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum      

arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4
n = 9

res = find_max(arr, n, k)
print(res)




def find_max(arr, n, k):
    # Compute the sum of the first window of size k
    max_sum = sum(arr[:k])
    current_sum = max_sum

    # Slide the window from the end of the first window to the end of the array
    for i in range(k, n):  # Start from k to n
        # Slide the window: subtract the element going out and add the new element coming in
        current_sum = current_sum - arr[i - k] + arr[i]
        
        # Update max_sum if current_sum is greater
        if current_sum > max_sum:
            max_sum = current_sum
    
    return max_sum

arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4
n = len(arr)  # Use the length of the array

res = find_max(arr, n, k)
print(res)  # This will print the maximum sum of any subarray of size k
