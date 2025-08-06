// Hardcoded input
let n = 10;
let arr = [9, 8, 4, 10, 3, 6, 5, 7, 1, 2];

// Sort the array
arr.sort((a, b) => a - b);

// Swap adjacent elements in pairs
for (let i = 0; i < n - 1; i += 2) {
    [arr[i], arr[i + 1]] = [arr[i + 1], arr[i]];
}

// Print the result
console.log(...arr);
