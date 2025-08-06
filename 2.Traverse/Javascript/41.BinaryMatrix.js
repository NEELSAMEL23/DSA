function binaryMatrix(arr, N, M) {
    for (let i = 0; i < N; i++) {
        let row = [];
        for (let j = 0; j < M; j++) {
            if (arr[i][j] === 1) {
                row.push(0);
            } else {
                row.push(1);
            }
        }
        console.log(...row);
    }
}

// Hardcoded input
let arr = [
    [1, 0],
    [0, 1],
    [1, 1]
];

let N = 3;
let M = 2;

binaryMatrix(arr, N, M);
