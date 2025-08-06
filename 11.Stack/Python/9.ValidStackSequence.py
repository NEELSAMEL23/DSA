def is_valid_stack_sequence(pushed, popped):
    stack = []
    j = 0
    
    for num in pushed:
        stack.append(num)

        while stack and stack[-1] == popped[j]:
            stack.pop()
            j += 1
    
    if stack:
        return "No"
    else:
        return "Yes"


n = 5
pushed = [1,2,3,4,5]
popped = [5,4,3,2,1]
result = is_valid_stack_sequence(pushed, popped)
print(result)
