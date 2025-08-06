# Sort the array first
A = [4, 1, 7, 4, 1, 4]
A.sort()

# Initialize two pointers and a variable to count pairs
i = 0
total_pairs = 0

# Traverse the sorted list
while i < len(A) - 1:
    if A[i] == A[i + 1]:  # If the current sock is the same as the next one
        total_pairs += 1
        i += 2  # Skip the next sock because we've already paired it
    else:
        i += 1  # Move to the next sock

# Output the result
print(total_pairs)
