def k_beauty_of_num_brute(num, k):
    num_str = str(num)
    count = 0

    # Generate all k-digit numbers
    for i in range(10**(k-1), 10**k):
        if str(i) in num_str and num % i == 0:
            count += num_str.count(str(i))  # Count how many times it appears

    return count

# Example usage
num = 430043
k = 2
res = k_beauty_of_num_brute(num, k)
print(res)




def k_beauty_of_num(num, k):
    # Convert the number to a string to easily extract substrings
    num_str = str(num)
    count = 0
    
    # Loop through the number string to extract all substrings of length k
    for i in range(len(num_str) - k + 1):
        # Extract the substring
        sub_str = num_str[i:i+k]
        # Convert substring to an integer
        sub_num = int(sub_str)
        
        # Check if the substring is a divisor of num and is not zero
        if sub_num != 0 and num % sub_num == 0:
            count += 1
    
    return count

num = 430043
k = 2
res = k_beauty_of_num(num, k)
print(res)