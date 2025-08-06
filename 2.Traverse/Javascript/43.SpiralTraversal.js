function spiralTraverse(matrix, N, M) {
    let top = 0;
    let bottom = N - 1;
    let left = 0;
    let right = M - 1;

    let arr = [];

    while (top <= bottom && left <= right) {
        // Traverse down along the leftmost column
        
        for (let i = top; i <= bottom; i++) {
            arr.push(matrix[i][left]);
        }

        left++;

        // Traverse right along the bottom row
        for (let j = left; j <= right; j++) {   
            arr.push(matrix[bottom][j]);
        }
        bottom--;

        if (left <= right) {
            // Traverse up along the rightmost column
            for (let i = bottom; i >= top; i--) {
                arr.push(matrix[i][right]);
            }
            right--;
        }

        if (top <= bottom) {
            // Traverse left along the top row
            for (let j = right; j >= left; j--) {
                arr.push(matrix[top][j]);
            }
            top++;
        }
    }

    return arr.join(" ");
}

// Hardcoded input
let matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
];

let N = 3;
let M = 4;

let res = spiralTraverse(matrix, N, M);
console.log(res);
