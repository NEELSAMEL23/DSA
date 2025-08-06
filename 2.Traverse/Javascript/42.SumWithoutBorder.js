function sumWithoutBorders(matrix, N, M) {
    let totalSum = 0;

    for (let i = 1; i < N - 1; i++) {
        for (let j = 1; j < M - 1; j++) {
            totalSum += matrix[i][j];
        }
    }

    return totalSum;
}

// Hardcoded input
let matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
];

let N = 3;
let M = 3;

let res = sumWithoutBorders(matrix, N, M);
console.log(res);
