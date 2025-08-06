def solve(n, arr):
    from collections import defaultdict

    count = defaultdict(int)
    left = 0
    max_len = 0

    for right in range(n):
        count[arr[right]] += 1

        while len(count) > 2:
            count[arr[left]] -= 1
            if count[arr[left]] == 0:
                del count[arr[left]]
            left += 1

        max_len = max(max_len, right - left + 1)

    print(max_len)
