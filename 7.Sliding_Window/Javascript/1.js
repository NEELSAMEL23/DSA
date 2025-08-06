function find_max(arr, n, k) {
    // Compute the sum of the first window of size k
    let max_sum = 0;
    for (let i = 0; i < k; i++) {
        max_sum += arr[i];
    }
    let current_sum = max_sum;

    // Slide the window from the end of the first window to the end of the array
    for (let i = k; i < n; i++) {
        current_sum = current_sum - arr[i - k] + arr[i];
        
        // Update max_sum if current_sum is greater
        if (current_sum > max_sum) {
            max_sum = current_sum;
        }
    }

    return max_sum;
}

let arr = [1, 4, 2, 10, 23, 3, 1, 0, 20];
let k = 4;
let n = arr.length;

let res = find_max(arr, n, k);
console.log(res); // Output: 39
