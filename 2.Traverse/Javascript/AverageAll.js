let n = 4;
let arr = [2, 5, 0, 9]; // removed the empty element

// Calculate sum
let sum = arr.reduce((acc, val) => acc + val, 0);

// Calculate average
let average = sum / n;

// Check if average is an integer
if (Number.isInteger(average)) {
    console.log(average);
} else {
    console.log(Math.ceil(average));
}
