function findDiagonals(matrix, N, M, K) {
    let row = -1;
    let col = -1;

    // Find position of element K
    for (let i = 0; i < N; i++) {
        for (let j = 0; j < M; j++) {
            if (matrix[i][j] === K) {
                row = i;
                col = j;
                break;
            }
        }
        if (row !== -1) break;
    }

    if (row === -1) {
        console.log("Element not found");
        return;
    }

    // Left-to-right diagonal (↘️)
    const leftToRightDiag = [];

    // Traverse upward-left
    let i = row, j = col;
    while (i >= 0 && j >= 0) {
        leftToRightDiag.unshift(matrix[i][j]);
        i--;
        j--;
    }

    // Traverse downward-right
    i = row + 1;
    j = col + 1;
    while (i < N && j < M) {
        leftToRightDiag.push(matrix[i][j]);
        i++;
        j++;
    }

    // Right-to-left diagonal (↙️)
    const rightToLeftDiag = [];

    // Traverse upward-right
    i = row;
    j = col;
    while (i >= 0 && j < M) {
        rightToLeftDiag.unshift(matrix[i][j]);
        i--;
        j++;
    }

    // Traverse downward-left
    i = row + 1;
    j = col - 1;
    while (i < N && j >= 0) {
        rightToLeftDiag.push(matrix[i][j]);
        i++;
        j--;
    }

    // Print both diagonals
    console.log(leftToRightDiag.join(" "));
    console.log(rightToLeftDiag.join(" "));
}

// Example usage:
const N = 4;
const M = 4;
const matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
];
const K = 11;

findDiagonals(matrix, N, M, K);
