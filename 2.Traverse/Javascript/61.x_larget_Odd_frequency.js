function checkLargestOddFrequencySingle(matrix, N) {
    const combinedDiags = [];


    for (let i = 0; i < N; i++) {
        combinedDiags.push(matrix[i][i]);
        combinedDiags.push(matrix[i][N - 1 - i]);
    }

    const maxElem = Math.max(...combinedDiags);

    let maxCount = 0;
    for (let num of combinedDiags) {
        if (num === maxElem) {
            maxCount++;
        }
    }

    if (maxCount % 2 === 1) {
        return "yes";
    } else {
        return "no";
    }
}

const N = 2;
const matrix = [
  [1,4],
  [4,4] // max = 100, appears once → odd
];

const res = checkLargestOddFrequencySingle(matrix, N);
console.log(res); // Output: "yes"
