def longest_well_performing_interval(scores):
    # Convert scores into a difference array
    # 1 for scores > 80 (good), -1 for scores <= 80 (non-good)
    score_diff = [1 if score > 80 else -1 for score in scores]

    # To store prefix sums and their first occurrence index
    prefix_sum_map = {}
    
    # Initialize variables
    prefix_sum = 0
    longest_interval = 0
    
    # Traverse the score_diff array
    for i, val in enumerate(score_diff):
        # Update the prefix sum
        prefix_sum += val
        
        # If prefix sum is positive, then we found a valid interval from 0 to i
        if prefix_sum > 0:
            longest_interval = i + 1
        else:
            # If prefix_sum <= 0, check for earlier occurrences in prefix_sum_map
            if prefix_sum - 1 in prefix_sum_map:
                longest_interval = max(longest_interval, i - prefix_sum_map[prefix_sum - 1])
        
        # Record the first occurrence of this prefix sum if not already recorded
        if prefix_sum not in prefix_sum_map:
            prefix_sum_map[prefix_sum] = i
    
    return longest_interval

# Example usage
scores = [90, 62, 67, 7, 62, 99, 60]
result = longest_well_performing_interval(scores)
print(result)
