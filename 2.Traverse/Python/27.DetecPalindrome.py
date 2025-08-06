def palindrome(num):
    original = num
    reversed_num = 0

    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num = num // 10  # Integer division

    if original == reversed_num:
        print("Yes")
    else:
        print("No")

# Example usage
palindrome(121)  # Output: Yes
palindrome(123)  # Output: No
