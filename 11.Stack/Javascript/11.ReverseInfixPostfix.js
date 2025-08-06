function postfixToInfix(postfix) {
    const stack = [];

    for (let char of postfix) {
        if (/[a-zA-Z]/.test(char)) {  // Check if it's an operand
            stack.push(char);
        } else {
            const operand2 = stack.pop();
            const operand1 = stack.pop();
            const newExpr = `(${operand1}${char}${operand2})`;
            stack.push(newExpr);
        }
    }

    return stack.pop()
}

const postfix = "ab+c-def-*g/+hij/*+";
const result = postfixToInfix(postfix);
console.log(result);
