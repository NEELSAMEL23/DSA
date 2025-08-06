def treasure_hunt(t, testcases):
    results = []
    for i in range(t):
        n, arr = testcases[i]
        left = 0
        right = n - 1
        left_sum = 0
        right_sum = 0
        max_equal = 0

        while left <= right:
            if left_sum == right_sum:
                max_equal = left_sum
            if left_sum <= right_sum:
                left_sum += arr[left]
                left += 1
            else:
                right_sum += arr[right]
                right -= 1

        if left_sum == right_sum:
            max_equal = left_sum

        results.append(max_equal)
    return results

# Example input processing
t = 2
testcases = [
    (3, [1, 7, 3]),
    (8, [5, 2, 5, 2, 1, 4, 6, 6])
]

print("\n".join(map(str, treasure_hunt(t, testcases))))
