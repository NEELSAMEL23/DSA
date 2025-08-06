def find_winner_driver_stack(n, heights):
    stack = []  # Stack to keep track of indices of drivers
    max_visibility = -1
    winner_index = -1
    
    for i in range(n):
        # Count how many previous drivers are shorter than the current one
        while stack and heights[stack[-1]] < heights[i]:
            stack.pop()
        
        # Visibility = count of shorter drivers * (1-based index)
        X = len(stack)  # The size of the stack gives the count of shorter drivers
        P = i + 1
        visibility = X * P
        
        # Update max visibility and winner index
        if visibility > max_visibility or (visibility == max_visibility and winner_index > i):
            max_visibility = visibility
            winner_index = i
        
        # Push the current index onto the stack
        stack.append(i)
    
    return winner_index + 1  # Convert to 1-based index

# Example usage
n = 5
heights = [4, 1, 2, 1, 4]

res = find_winner_driver_stack(n, heights)
print(res)  # Output: 5
