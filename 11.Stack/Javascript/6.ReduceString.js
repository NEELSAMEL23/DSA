function reduceString(s) {
    const stack = [];

    for (let char of s) {
        if (stack.length > 0 && stack[stack.length - 1] === char) {
            stack.pop(); // Remove the previous char (they cancel out)
        } else {
            stack.push(char);
        }
    }

    const result = stack.join('');
    console.log(result === '' ? "Empty String" : result);
}

// Hardcoded input
const s = "aaabccddd";
reduceString(s);
