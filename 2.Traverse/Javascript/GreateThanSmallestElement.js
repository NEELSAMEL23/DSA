let n = 5;
let arr = [3, 2, 2, 1, 1];

// Find the minimum value
let min_val = Math.min(...arr);

// Replace elements greater than min_val with -1
for (let i = 0; i < n; i++) {
    if (arr[i] > min_val) {
        arr[i] = -1;
    }
}

// Print the result
console.log(...arr); // or console.log(arr.join(" "))
