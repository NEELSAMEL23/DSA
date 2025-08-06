def process_string(s):
    stack = []
    for char in s:
        if char == '#':
            if stack:
                stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)

def smart_teacher():
    answer = "ab#c"
    solution = "ad#c"

    final_answer = process_string(answer)
    final_solution = process_string(solution)

    if final_answer == final_solution:
        print("CORRECT")
    else:
        print("WRONG")

# Run the function
smart_teacher()
