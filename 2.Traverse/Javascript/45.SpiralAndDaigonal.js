function spiralMatrix(n, arr) {
    const matrix = Array.from({ length: n }, () => Array(n).fill(0));

    let top = 0, bottom = n - 1;
    let left = 0, right = n - 1;
    let index = 0;

    while (index < arr.length) {
        // Left to right
        for (let i = left; i <= right && index < arr.length; i++) {
            matrix[top][i] = arr[index++];
        }
        top++;

        // Top to bottom
        for (let i = top; i <= bottom && index < arr.length; i++) {
            matrix[i][right] = arr[index++];
        }
        right--;

        // Right to left
        for (let i = right; i >= left && index < arr.length; i--) {
            matrix[bottom][i] = arr[index++];
        }
        bottom--;

        // Bottom to top
        for (let i = bottom; i >= top && index < arr.length; i--) {
            matrix[i][left] = arr[index++];
        }
        left++;
    }

    return matrix;
}

function sumOfDiagonals(matrix, n) {
    let sum = 0;

    for (let i = 0; i < n; i++) {
        sum += matrix[i][i]; // Main diagonal

        if (i !== n - i - 1) {
            sum += matrix[i][n - i - 1]; // Anti-diagonal (skip center if same)
        }
    }

    return sum;
}

// Example usage
const arr = [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10];
const N = 4;

const matrix = spiralMatrix(N, arr);
const res = sumOfDiagonals(matrix, N);

console.log(res); // Output: 68
