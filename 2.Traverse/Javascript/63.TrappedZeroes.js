function countTrappedZeroes(n, m, arr) {
    if (n < 3 || m < 3) {
        console.log(0);
        return;
    }

    let count = 0;

    for (let i = 1; i < n - 1; i++) {
        for (let j = 1; j < m - 1; j++) {
            if(arr[i][j] === 0 && arr[i - 1][j] === 1 && arr[i + 1][j] === 1 && arr[i][j - 1] === 1 && arr[i][j + 1] === 1){
                count++;
            }
        }
    }

    console.log(count);
}

// Hardcoded input
const n = 3;
const m = 3;
const arr = [
    [1, 1, 1],
    [0, 1, 0],
    [1, 0, 1]
];

const res = countTrappedZeroes(n, m, arr);
console.log("Trapped zeroes count:", res);
