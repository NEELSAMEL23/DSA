def longest_beautiful_substring(s, k):
    max_len = 0
    n = len(s)
    
    for target in set(s):  # optimize by only using characters present in string
        left = 0
        count = 0
        
        for right in range(n):
            if s[right] != target:
                count += 1
            
            while count > k:
                if s[left] != target:
                    count -= 1
                left += 1
            
            max_len = max(max_len, right - left + 1)
    
    return max_len

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    S = input()
    print(longest_beautiful_substring(S, K))
