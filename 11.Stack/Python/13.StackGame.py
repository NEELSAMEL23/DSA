def Parentheses_Stack_Game(S):
    stack = []
    for char in S:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack:
                return "no"
            stack.pop()
    return "yes" if not stack else "no"

# ----- SINGLE HARDCODED INPUT -----
N, M = 4, 4
S = "(())"

print(Parentheses_Stack_Game(S))
