def postfix_to_infix(postfix):
    stack = []
    
    for char in postfix:
        if char.isalpha():  
            stack.append(char)
        else: 
            operand2 = stack.pop()
            operand1 = stack.pop()
        
            new_expr = f"({operand1}{char}{operand2})"
            stack.append(new_expr)
    
  
    return stack.pop()

postfix = "ab+c-def-*g/+hij/*+"
res = postfix_to_infix(postfix)
print(res)