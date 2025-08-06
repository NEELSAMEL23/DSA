// 🔽 Hardcoded single input
const n = 5;
const A = [3,1,4,5,4];  // A[i] is who i+1 called

const called = new Set();

for (let i = 0; i < n; i++) {
    const current_id = i + 1;
    if (!called.has(current_id)) {
        called.add(A[i]);
    }
}

const never_called = [];
for (let i = 1; i <= n; i++) {
    if (!called.has(i)) {
        never_called.push(i);
    }
}

// Output
console.log(never_called.length);
console.log(never_called.sort((a, b) => a - b).join(" "));
