def three_sum(nums):
    nums.sort()
    n = len(nums)
    result = set()

    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = n - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                triplet = tuple(sorted((nums[i], nums[left], nums[right])))
                result.add(triplet)
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1

    # Sort the result overall and print
    result = sorted(list(result))
    print(len(result))
    for triplet in result:
        print(*triplet)

# 🔸 Hardcoded input
nums = [0, 1, 2, -1, -4, -1]

# 🔸 Function call
three_sum(nums)
