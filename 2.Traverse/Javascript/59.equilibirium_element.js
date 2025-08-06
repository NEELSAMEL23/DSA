function solve(N, A) {
    const total_sum = A.reduce((a, b) => a + b, 0);
    let left_sum = 0;
    let found = false;

    for (let i = 1; i < N - 1; i++) {
        left_sum += A[i - 1];
        const right_sum = total_sum - left_sum - A[i];

        if (left_sum === right_sum) {
            console.log(i); // 0-based index
            found = true;
            break;
        }
    }

    if (!found) {
        console.log(-1);
    }
}

// 🔽 Hardcoded input
const n = 5;
const arr = [15, 1, 5, 5, 5];

solve(n, arr);  // Output: 1
