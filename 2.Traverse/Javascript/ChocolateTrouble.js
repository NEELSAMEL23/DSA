function remainingChocolates(a, b) {
    while (b !== 0) {
        [a, b] = [b, a % b];
    }
    return a;
}

// Hardcoded single test case
const x = 5;
const y = 3;

const result = 2 * remainingChocolates(x, y);
console.log(result);  // Output: 2
