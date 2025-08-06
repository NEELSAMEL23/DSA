def reduce_string(s):
    stack = []
    
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()  # Remove the previous char (they cancel out)
        else:
            stack.append(char)
    
    result = ''.join(stack)
    print(result if result else "Empty String")

# Hardcoded input
s = "aaabccddd"
reduce_string(s)
