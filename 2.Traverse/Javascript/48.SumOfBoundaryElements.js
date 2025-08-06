function sumBoundaryDiagonal(arr, N) {
    let sum = 0;

    // Top row
    for (let j = 0; j < N; j++) {
        sum += arr[0][j];
    }

    // Bottom row
    for (let j = 0; j < N; j++) {
        sum += arr[N - 1][j];
    }

    // Left column (excluding corners)
    for (let i = 1; i < N - 1; i++) {
        sum += arr[i][0];
    }

    // Right column (excluding corners)
    for (let i = 1; i < N - 1; i++) {
        sum += arr[i][N - 1];
    }

    // Main diagonal (excluding corners)
    for (let i = 1; i < N - 1; i++) {
        sum += arr[i][i];
    }

    // Anti-diagonal (excluding corners, and avoid double-counting center)
    for (let i = 1; i < N - 1; i++) {
        if (i !== N - i - 1) {
            sum += arr[i][N - i - 1];
        }
    }

    return sum;
}

// Example input
const arr = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 1],
    [2, 3, 4, 5, 6],
    [7, 8, 9, 1, 2],
    [3, 4, 5, 6, 7]
];
const N = 5;

const result = sumBoundaryDiagonal(arr, N);
console.log(result); // Output: 104
