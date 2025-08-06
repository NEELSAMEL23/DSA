let N = 3;
let X = 2;

let sum = 0;
for (let i = 0; i < N; i++) {
    sum += X ** i;
}

console.log(sum);

// DRY RUN:
// 2 ** 0 = 1
// 2 ** 1 = 2
// 2 ** 2 = 4
// sum = 1 + 2 + 4 = 7
