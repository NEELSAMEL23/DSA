function odd_sums_column(arr, N, M) {
    for (let j = 0; j < M; j++) { 
        let sum = 0;
        for (let i = 0; i < N; i++) { 
            if (arr[i][j] % 2 !== 0) { // Check if the element is odd
                sum += arr[i][j];
            }
        }
        console.log(`Column ${j}:`, sum); // Print sum of odd numbers for column j
    }
}

// Example usage
const N = 3;
const M = 3;
const arr = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
];

odd_sums_column(arr, N, M);
