
function setZeroes(n, m, matrix) {
    const rows = new Array(n).fill(false);
    const cols = new Array(m).fill(false);

    // First pass: record the rows and columns that need to be zeroed
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            if (matrix[i][j] === 0) {
                rows[i] = true;
                cols[j] = true;
            }
        }
    }

    // Second pass: set the cells to zero if their row or column was marked
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            if (rows[i] || cols[j]) {
                matrix[i][j] = 0;
            }
        }
    }

    // Output the modified matrix
    for (let i = 0; i < n; i++) {
        console.log(matrix[i].join(" "));
    }
}




const n = 3;
const m = 3;
const matrix = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
];

setZeroes(n, m, matrix);
