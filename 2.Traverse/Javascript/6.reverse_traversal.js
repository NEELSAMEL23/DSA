function reverseTraversal(n, arr) {
    let matrix = [];
    for (let i = n - 1; i >= 0; i--) {
        matrix.push(arr[i]);
    }
    return matrix;
}

let n = 5;
let arr = [1, 3, 2, 4, 5];
let res = reverseTraversal(n, arr);
console.log(...res);
