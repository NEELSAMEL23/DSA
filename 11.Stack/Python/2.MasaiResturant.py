def stack_operations(operations,n):

    stack = []
    result = []

    for operation in operations:
        if operation[0] == "1":
            if stack:
                result.append(str(stack.pop()))
            else:
                result.append("No Food")
        elif operation[0] == "2":
            _,x = operation.split()
            stack.append(int(x))

    return "\n".join(result)

operations = ["1","2 5", "2 7", "2 9", "1", "1"]
n = 5

res = stack_operations(operations,n)
print(res)
# Output:-
# No Food
# 9
# 7