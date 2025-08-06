function zTraversal(matrix, N) {
    // Print first row
    for (let i = 0; i < N; i++) {
        process.stdout.write(matrix[0][i] + " ");
    }

    // Print diagonal from top-right to bottom-left (excluding first and last rows)
    for (let i = 1; i < N - 1; i++) {
        process.stdout.write(matrix[i][N - i - 1] + " ");
    }

    // Print last row
    for (let i = 0; i < N; i++) {
        process.stdout.write(matrix[N - 1][i] + " ");
    }

    console.log(); // Move to next line after output
}

// Hardcoded input
let matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
];
let N = 3;

zTraversal(matrix, N);
