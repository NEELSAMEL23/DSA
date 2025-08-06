def stack_operations(operations,n):

    stack = []
    result = []

    for operation in operations:
        if operation[0] == "1":
            _,x = operation.split()
            stack.append(int(x))
        elif operation[0] == "2":
            if stack:
                stack.pop() 
        elif operation[0] == "3":
            if stack:
                result.append(str(stack[-1]))
            else:
                result.append("Empty!")

    return "\n".join(result)

operations = ["1 15", "1 20", "2", "3", "2","3"]
n = 5

res = stack_operations(operations,n)
print(res)

# Output:-
# 15    
# Empty!