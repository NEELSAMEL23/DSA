def longestSubstring(s, k):
    n = len(s)
    max_len = 0

    # Iterate through all possible substrings
    for i in range(n):
        for j in range(i + 1, n + 1):
            # Step 1: Get the substring
            substring = s[i:j]
            
            # Step 2: Create a dictionary to store character counts
            char_counts = {}
            for char in substring:
                # Count each character in the substring
                if char in char_counts:
                    char_counts[char] += 1
                else:
                    char_counts[char] = 1
            
            # Step 3: Check if every character appears at least k times
            valid = True
            for count in char_counts.values():
                if count < k:
                    valid = False
                    break  # No need to check further if one character fails
            
            # Step 4: Update max_len if substring meets the condition
            if valid:
                max_len = max(max_len, j - i)

    return max_len

# Example usage
s = "aaabb"
k = 3
res = longestSubstring(s, k)
print(res)



def longestSubstring(s, k):
    # Base case: if string length is less than k, no valid substring
    if len(s) < k:
        return 0
    
    # Count frequency of each character in the string
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    
    # Find a character with frequency less than k
    for char in freq:
        if freq[char] < k:
            # Split the string at that character and solve for each part
            return max(longestSubstring(sub, k) for sub in s.split(char))
    
    # If every character appears at least k times, return the whole string length
    return len(s)



s = "aaabb"
k = 3
res = longestSubstring(s,k)
print(res)