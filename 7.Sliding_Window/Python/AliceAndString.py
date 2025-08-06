def max_beauty(s, k, target_char):
    left = 0
    max_len = 0
    count = 0 

    for right in range(len(s)):
        if s[right] != target_char:
            count += 1

        while count > k:
            if s[left] != target_char:
                count -= 1
            left += 1
        
        max_len = max(max_len, right - left + 1)
    
    return max_len


n, k = map(int, input().split())
s = input()


result = max(max_beauty(s, k, '0'), max_beauty(s, k, '1'))
print(result)
