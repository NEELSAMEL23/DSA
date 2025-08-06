def unique_count(arr, n):
    # Set to store unique elements in the current subarray
    unique_gifts = set()

    # Variables to track the maximum length and the two pointers i and j
    max_length = 0
    i = 0

    # Move j (the second pointer) from 0 to n
    for j in range(n):
        # If arr[j] is a duplicate, move i to the right until we remove the duplicate
        while arr[j] in unique_gifts:
            unique_gifts.remove(arr[i])
            i += 1
        
        # Add arr[j] to the set
        unique_gifts.add(arr[j])
        
        # Calculate the length of the current subarray and update max_length
        max_length = max(max_length, j - i + 1)
    
    # Return the maximum length of a subarray with unique elements
    return max_length

# Example usage
arr = [1, 2, 1, 3, 2, 7, 4, 2]
n = len(arr)  # Length of the array
result = unique_count(arr, n)
print(result)  # Output: 5
