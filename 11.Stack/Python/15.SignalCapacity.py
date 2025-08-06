def signal_ranges(heights):
    n = len(heights)
    stack = []
    res = []

    for i in range(n):
        while stack and heights[stack[-1]] <= heights[i]:
            stack.pop()

        if not stack:
            res.append(i + 1)
        else:
            res.append(i - stack[-1])

        stack.append(i)

    return res


# Single hardcoded input
heights = [100, 80, 60, 70, 60, 75, 85]
result = signal_ranges(heights)
print(' '.join(map(str, result)))
