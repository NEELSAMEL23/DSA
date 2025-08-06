def pattern_count():
    T = int(input())  # Number of test cases
    for _ in range(T):
        N, M = map(int, input().split())  # Length of word and pattern
        word = input().strip()
        pattern = input().strip()

        count = 0
        # Slide over the word and compare substrings of length M
        for i in range(N - M + 1):
            if word[i:i+M] == pattern:
                count += 1
        print(count)

# Example usage:
# Input:
# 2
# 5 2
# aaabb
# aa
# 7 3
# aaabaaa
# baa
# Output:
# 2
# 1

pattern_count()
