function counterclockwiseSpiralTraversal(matrix, N, M) {
    let top = 0, bottom = N - 1;
    let left = 0, right = M - 1;

    const result = [];

    while (top <= bottom && left <= right) {
        // Bottom to top on leftmost column
        for (let i = bottom; i >= top; i--) {
            result.push(matrix[i][left]);
        }
        left++;

        // Left to right on top row
        if (left <= right) {
            for (let i = left; i <= right; i++) {
                result.push(matrix[top][i]);
            }
            top++;
        }

        // Top to bottom on rightmost column
        if (top <= bottom) {
            for (let i = top; i <= bottom; i++) {
                result.push(matrix[i][right]);
            }
            right--;
        }

        // Right to left on bottom row
        if (left <= right) {
            for (let i = right; i >= left; i--) {
                result.push(matrix[bottom][i]);
            }
            bottom--;
        }
    }

    console.log(result.join(" "));
}

// Example usage:
const matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
];
const N = 3;
const M = 4;

counterclockwiseSpiralTraversal(matrix, N, M);
