function smallestFrequency(matrix, N) {
    let diagElemen = [];

    for (let i = 0; i < N; i++) {
        diagElemen.push(matrix[i][i]);              // Primary diagonal
        diagElemen.push(matrix[i][N - 1 - i]);      // Secondary diagonal
    }

    let minVal = Math.min(...diagElemen);
    let res = diagElemen.filter(x => x === minVal).length;

    return res;
}

let N = 2;
let matrix = [
    [1, 1],
    [3, 4]
];

let res = smallestFrequency(matrix, N);
console.log(res);  // Output: 2
