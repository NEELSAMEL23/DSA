function processString(s) {
    const stack = [];
    for (const char of s) {
        if (char === '#') {
            if (stack.length > 0) {
                stack.pop();
            }
        } else {
            stack.push(char);
        }
    }
    return stack.join('');
}


const answer = "ab#c";
const solution = "ad#c";

const finalAnswer = processString(answer);
const finalSolution = processString(solution);

if (finalAnswer === finalSolution) {
    console.log("CORRECT");
} else {
    console.log("WRONG");
}

