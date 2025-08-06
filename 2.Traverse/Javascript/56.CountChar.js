function countChars(s) {
    let result = "";
    let count = 1;

    for (let i = 1; i <= s.length; i++) {
        if (s[i] === s[i - 1]) {
            count++;
        } else {
            result += s[i - 1] + count;
            count = 1;
        }
    }

    console.log(result);
}

// Example usage:
countChars("aaabbbbcc");  // Output: a3b4c2

