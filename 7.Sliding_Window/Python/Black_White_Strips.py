def min_repaints(n, k, stripe):
    left = 0
    current_w_count = 0
    min_repaints = float('inf')

    # Initialize the window and count 'W' in the first window
    for right in range(k):
        if stripe[right] == 'W':
            current_w_count += 1

    # The first window is processed
    min_repaints = current_w_count

    # Slide the window using two pointers (left and right)
    for right in range(k, n):
        # Move the left pointer and adjust the window
        if stripe[left] == 'W':
            current_w_count -= 1
        left += 1

        # Move the right pointer and adjust the window
        if stripe[right] == 'W':
            current_w_count += 1

        # Update the minimum number of repaints
        min_repaints = min(min_repaints, current_w_count)

    return min_repaints

stripe = "BBWBW"
n = 5
k = 5
res = min_repaints(n, k, stripe)
print(res)