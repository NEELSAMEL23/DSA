def count_substrings(s):
    char_map = {}
    start = 0
    count = 0
    

    for end in range(len(s)):
        
        if s[end] in char_map and char_map[s[end]] >= start:
            start = char_map[s[end]] + 1
        
        
        count += (end - start + 1)

        char_map[s[end]] = end
    
    return count


t = int(input())
for i in range(t):
    s = input()
    print(count_substrings(s))
