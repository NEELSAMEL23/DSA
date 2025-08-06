function traverseArr(arr, N, M) {
    let sum = 0;

    for (let i = 0; i < N; i++) {
        sum += arr[i][0];       // First column
        sum += arr[i][M - 1];   // Last column
    }

    return sum;
}

// Hardcoded 2D array
let arr = [
    [1, 2, 7],
    [3, 4, 6],
    [5, 6, 10]
];

let N = 3;
let M = 3;

let res = traverseArr(arr, N, M);
console.log(res);  // Output: 1+7 + 3+6 + 5+10 = 32
