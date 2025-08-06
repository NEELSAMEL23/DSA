function maxRow(arr, N, M) {
  const result = [];

  for (let i = 0; i < N; i++) {
    let maxInRow = arr[i][0]; // Start with the first element of the row

    for (let j = 1; j < M; j++) {
      if (arr[i][j] > maxInRow) {
        maxInRow = arr[i][j];
      }
    }

    result.push(maxInRow);
  }

  return result;
}

// Example input
const N = 3;
const M = 3;
const arr = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
];

const res = maxRow(arr, N, M);
console.log(...res); // Output: 3 6 9
