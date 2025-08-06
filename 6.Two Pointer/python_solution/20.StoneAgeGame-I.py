def stone_age_game(stones):
    # Number of boxes
    num_boxes = len(stones)

    # Initialize pointers and accumulators
    left_ptr, right_ptr = 0, num_boxes - 1
    left_sum, right_sum = stones[left_ptr], stones[right_ptr]
    left_boxes, right_boxes = 1, 1
    
    # Maximum difference in number of boxes covered
    max_box_difference = -1
    
    while left_ptr < right_ptr:
        # If both have the same amount of stones
        if left_sum == right_sum:
            max_box_difference = max(max_box_difference, abs(left_boxes - right_boxes))
            left_ptr += 1
            right_ptr -= 1
            if left_ptr < right_ptr:
                left_sum += stones[left_ptr]
                right_sum += stones[right_ptr]
                left_boxes += 1
                right_boxes += 1
        elif left_sum < right_sum:
            # Move Ram (left pointer) one step
            left_ptr += 1
            if left_ptr < right_ptr:
                left_sum += stones[left_ptr]
                left_boxes += 1
        else:
            # Move Shyam (right pointer) one step
            right_ptr -= 1
            if left_ptr < right_ptr:
                right_sum += stones[right_ptr]
                right_boxes += 1

    # If they never achieve the same number of stones
    if max_box_difference == -1 and left_sum != right_sum:
        return -1
    else:
        return max_box_difference

# Example usage
stones = [100, 1, 2, 5, 8, 97, 2, 1]
result = stone_age_game(stones)
print(result)
