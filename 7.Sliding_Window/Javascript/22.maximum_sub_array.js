function maxSubarraySum(N, arr) {
    let maxSum = -Infinity;
    let currentSum = 0;

    for (let i = 0; i < N; i++) {
        currentSum += arr[i];
        maxSum = Math.max(maxSum, currentSum);
        if (currentSum < 0) {
            currentSum = 0;
        }
    }

    return maxSum;
}

let N = 5;
let arr = [1, 2, 0, 4, 5];
let res = maxSubarraySum(N, arr);
console.log(res);  // Output: 12
