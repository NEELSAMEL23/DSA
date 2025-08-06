function oddCount(arr, N) {
    let odd_count = 0;

    for (let i = 0; i < N; i++) {
        if (arr[i] % 2 !== 0) {
            odd_count += 1;
        }
    }

    if (odd_count % 2 !== 0) {
        return "YES";
    }
    return "NO";
}

// Hardcoded input
let arr = [1, 101];
let N = 2;

let res = oddCount(arr, N);
console.log(res);
