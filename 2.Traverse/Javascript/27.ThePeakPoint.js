function findPeakPoint(arr, n) {
    for (let i = 1; i < arr.length - 1; i++) {
        if (arr[i] > arr[i - 1] && arr[i] > arr[i + 1]) {
            return i;
        }
    }
    return -1;
}

// Single hardcoded input
let n = 5;
let arr = [1, 3, 2, 4, 1];

let res = findPeakPoint(arr, n);
console.log(res);  // Output: 1
