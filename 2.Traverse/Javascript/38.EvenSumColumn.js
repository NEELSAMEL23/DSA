function traverseArr(arr, N, M) {
    for (let col = 0; col < M; col++) {
        let evenSum = 0;
        for (let row = 0; row < N; row++) {
            if (arr[row][col] % 2 === 0) {
                evenSum += arr[row][col];
            }
        }
        console.log(evenSum);
    }
}

// Hardcoded 2D array
let arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
];

let N = 3;
let M = 3;

traverseArr(arr, N, M);
