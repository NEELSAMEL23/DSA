function isPalindrome(s) {
    let stack = [];

    // Push all characters of the string onto the stack
    for (let char of s) {
        stack.push(char);
    }

    // Pop characters from the stack and form the reversed string
    let reversed_s = "";
    while (stack.length > 0) {
        reversed_s += stack.pop();
    }

    // Compare the original string with the reversed string
    if (s.toLowerCase() === reversed_s.toLowerCase()) {
        return "YES";
    } else {
        return "NO";
    }
}

// Example usage
const string = "MOM";
const res = isPalindrome(string);

console.log(res);
