def just_find_minimum(operations):
    mainStack = []
    minStack = []
    
    for op in operations:
        if op.startswith("PUSH"):
            _, value = op.split()
            value = int(value)
            mainStack.append(value)
            if not minStack or value <= minStack[-1]:
                minStack.append(value)
            else:
                minStack.append(minStack[-1])

        elif op == "POP":
            if not mainStack:
                print("EMPTY")
            else:
                mainStack.pop()
                minStack.pop()

        elif op == "MIN":
            if not minStack:
                print("EMPTY")
            else:
                print(minStack[-1])

# Sample usage
n = 11
ops = [
    "PUSH 5", "PUSH 7", "PUSH 3", "PUSH 8", "PUSH 10",
    "MIN", "POP", "POP", "MIN", "POP", "MIN"
]
just_find_minimum(ops)
