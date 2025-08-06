function solve(string) {
    let result = [];
    let count = 1;

    for (let i = 1; i < string.length; i++) {
        if (string[i] === string[i - 1]) {
            count++;
        } else {
            result.push(string[i - 1] + count);
            count = 1;
        }
    }

    result.push(string[string.length - 1] + count);
    const res = result.join('');
    console.log(res);
}

// Hardcoded input
solve("aaabbbbcc"); // Output: a3b4c2
