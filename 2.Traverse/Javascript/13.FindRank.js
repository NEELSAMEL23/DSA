function findRank(arr, N) {
    for (let i = 0; i < N; i++) {
        if (arr[i] === "India") {
            return i + 1;
        }
    }
}

let arr = ["Russia", "USA", "Japan", "China", "India"];
let N = 5;
let res = findRank(arr, N);
console.log(res);
