function countSumOccurrences(matrix, n, m, s) {
    let count = 0;

    // Horizontal check
    for (let i = 0; i < n; i++) {
        for (let j = 0; j <= m - 3; j++) {
            if (matrix[i][j] + matrix[i][j + 1] + matrix[i][j + 2] === s) {
                count++;
            }
        }
    }

    // Vertical check
    for (let i = 0; i <= n - 3; i++) {
        for (let j = 0; j < m; j++) {
            if (matrix[i][j] + matrix[i + 1][j] + matrix[i + 2][j] === s) {
                count++;
            }
        }
    }

    // Major diagonal check
    for (let i = 0; i <= n - 3; i++) {
        for (let j = 0; j <= m - 3; j++) {
            if (matrix[i][j] + matrix[i + 1][j + 1] + matrix[i + 2][j + 2] === s) {
                count++;
            }
        }
    }

    // Minor diagonal check
    for (let i = 2; i < n; i++) {
        for (let j = 0; j <= m - 3; j++) {
            if (matrix[i][j] + matrix[i - 1][j + 1] + matrix[i - 2][j + 2] === s) {
                count++;
            }
        }
    }

    return count;
}

// Example usage
const n = 3;
const m = 3;
const s = 6;
const matrix = [
    [3, 2, 1],
    [2, 2, 2],
    [1, 5, 1]
];

const result = countSumOccurrences(matrix, n, m, s);
console.log(result); // Expected output: 4
