def is_palindrome(s):
    return s == s[::-1]

def longest_palindromic_substring_length(s):
    max_len = 0
    n = len(s)
    for i in range(n):
        for j in range(i, n):
            if is_palindrome(s[i:j+1]):
                max_len = max(max_len, j - i + 1)
    return max_len

s = input().strip()
print(longest_palindromic_substring_length(s))
