function rotate90(matrix, N) {
    let result = [];

    for (let col = N - 1; col >= 0; col--) {
        let rowList = [];
        for (let row = 0; row < N; row++) {
            rowList.push(matrix[row][col]);
        }
        result.push(rowList);
    }

    // Print the rotated matrix
    for (let row of result) {
        console.log(row.join(" "));
    }
}

// Hardcoded input
let matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [1, 2, 3, 4],
    [5, 6, 7, 8]
];

let N = 4;

rotate90(matrix, N);
