def next_smaller_of_next_greater(arr):
    n = len(arr)
    nge = [-1] * n  # Next Greater Element indices
    nse = [-1] * n  # Next Smaller Element indices
    stack1 = []
    stack2 = []

    # Step 1: Find NGE (Next Greater Element)
    for i in range(n - 1, -1, -1):
        while stack1 and arr[stack1[-1]] <= arr[i]:
            stack1.pop()
        if stack1:
            nge[i] = stack1[-1]
        stack1.append(i)

    # Step 2: Find NSE (Next Smaller Element)
    for i in range(n - 1, -1, -1):
        while stack2 and arr[stack2[-1]] >= arr[i]:
            stack2.pop()
        if stack2:
            nse[i] = stack2[-1]
        stack2.append(i)

    # Step 3: Result = NSE of NGE
    result = []
    for i in range(n):
        next_greater_idx = nge[i]
        if next_greater_idx != -1:
            next_smaller_idx = nse[next_greater_idx]
            if next_smaller_idx != -1:
                result.append(arr[next_smaller_idx])
            else:
                result.append(-1)
        else:
            result.append(-1)

    return result

# Example usage
arr = [5, 1, 6, 2, 5, 1]
print(*next_smaller_of_next_greater(arr))  # Output: 2 2 -1 1 -1 -1
