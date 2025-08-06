function Parentheses_Stack_Game(S) {
    const stack = [];

    for (let char of S) {
        if (char === "(") {
            stack.push(char);
        } else if (char === ")") {

            if (stack.length === 0) {
                return "no";
            }
             
            stack.pop();
        }
    }

    return stack.length === 0 ? "yes" : "no";
}


const S = "(())";

console.log(Parentheses_Stack_Game(S));
