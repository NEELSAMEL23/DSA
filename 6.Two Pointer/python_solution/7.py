def lifeboats_needed(weights, n, k):
    # Step 1: Sort the list of weights in ascending order
    # This allows us to consider the lightest and heaviest person together.
    weights.sort()
    
    # Initialize two pointers:
    # 'left' starts from the beginning (lightest person)
    left = 0
    # 'right' starts from the end (heaviest person)
    right = n - 1
    
    # Counter to keep track of the number of boats needed
    boats = 0

    # Step 2: Use a while loop to pair people until all are assigned to boats
    while left <= right:
        # Check if the current lightest and heaviest person can share a boat
        if weights[left] + weights[right] <= k:
            # If they can share a boat, move both pointers:
            # Increase 'left' to point to the next lightest person
            left += 1
            # Decrease 'right' to point to the next heaviest person
            right -= 1
        else:
            # If they can't share a boat (i.e., their combined weight exceeds the limit),
            # only take the heavier person in the current boat (as the lighter person can't fit with them).
            # Move 'right' pointer to the next heaviest person
            right -= 1
        
        # In both cases (whether they share a boat or not), we used one boat
        boats += 1
    
    # Step 3: Return the total number of boats needed
    return boats



arr = [3, 5, 4,3] 
n = 4
k=5
res = lifeboats_needed(arr,n,k)
print(res)

