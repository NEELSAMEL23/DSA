def next_permutation(nums):
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    if i >= 0:
        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1:] = reversed(nums[i + 1:])
    return nums

n = int(input())
for _ in range(n):
    m = int(input())
    nums = list(map(int, input().split()))
    result = next_permutation(nums)
    print(" ".join(map(str, result)))
