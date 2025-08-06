function removeDuplicates(s) {
    const stack = [];
    
    for (let char of s) {
        if (stack.length > 0 && stack[stack.length - 1] === char) {
            stack.pop();
        } else {
            stack.push(char);
        }
    }

    return stack.join('');
}

const string = "abbaca";
const res = removeDuplicates(string);
console.log(res);  // Output: ca
