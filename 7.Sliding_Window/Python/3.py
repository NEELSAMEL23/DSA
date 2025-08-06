def min_expenses_brute_force(arr, n, k):
    min_sum = float('inf')  # Initialize to infinity to find the minimum

    # Traverse each possible subarray of size k
    for i in range(n - k + 1):
        current_sum = 0

        # Calculate sum of subarray starting from index i
        for j in range(i, i + k):
            current_sum += arr[j]
        
        # Update min_sum if we found a smaller sum
        min_sum = min(min_sum, current_sum)
        
    return min_sum



def min_expenses(arr, n, k):

    current_sum = sum(arr[:k])
    min_sum = current_sum


    for i in range(k, n):
        
        current_sum = current_sum - arr[i - k] + arr[i]

        min_sum = min(min_sum, current_sum)

    return min_sum


arr = [9,9,-5,9,5]
n = 5
k = 3

res = min_expenses(arr, n, k)
print(res)
