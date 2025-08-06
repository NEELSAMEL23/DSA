def count_substrings_with_k_distinct_bruteforce(s, n, k):
    count = 0
    
    # Iterate over all possible starting points
    for start in range(n):
        # Create a set to keep track of distinct characters
        distinct_chars = set()
        
        # Iterate over all possible ending points
        for end in range(start, n):
            distinct_chars.add(s[end])
            
            # If the number of distinct characters is equal to k, increment the count
            if len(distinct_chars) == k:
                count += 1
            # If the number of distinct characters exceeds k, break the loop
            elif len(distinct_chars) > k:
                break

    return count

s= "abcc"
n=4
k=2
res = count_substrings_with_k_distinct_bruteforce(s, n, k)
print(res)


def count_substrings_with_k_distinct(s, n, k):
   
    char_count = {}
    count = 0  
    window_start = 0 

 
    for window_end in range(n):
      
        char_count[s[window_end]] = char_count.get(s[window_end], 0) + 1
        

        if window_end - window_start + 1 > k:
            char_count[s[window_start]] -= 1
            if char_count[s[window_start]] == 0:
                del char_count[s[window_start]]
            window_start += 1
        
      
        if window_end - window_start + 1 == k and len(char_count) == k:
            count += 1

    return count



n, k = map(int, input().split()) 
s = input().strip() 

result = count_substrings_with_k_distinct(s, n, k)
print(result)


