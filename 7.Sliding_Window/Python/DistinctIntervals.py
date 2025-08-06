def count_unique_substrings(s):
    left = 0
    seen = set()
    total = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        total += right - left + 1
    return total

# Input Reading
T = int(input())
for _ in range(T):
    S = input().strip()
    print(count_unique_substrings(S))
