def min_length_max_distinct_substring(s):
    from collections import defaultdict

    n = len(s)
    max_distinct = len(set(s))  # count of distinct characters in full string

    freq = defaultdict(int)
    left = 0
    min_len = n

    count = 0  # count of distinct chars in current window

    for right in range(n):
        char = s[right]
        freq[char] += 1
        if freq[char] == 1:
            count += 1

        while count == max_distinct:
            min_len = min(min_len, right - left + 1)
            freq[s[left]] -= 1
            if freq[s[left]] == 0:
                count -= 1
            left += 1

    return min_len


# Input
s = input().strip()
print(min_length_max_distinct_substring(s))
