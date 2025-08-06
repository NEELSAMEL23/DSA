function solve(n, arr) {
    const answers = new Array(n).fill(0);
    const stack = [];

    for (let day = n - 1; day >= 0; day--) {
        while (stack.length && arr[day] >= arr[stack[stack.length - 1]]) {
            stack.pop();
        }

        if (stack.length) {
            answers[day] = stack[stack.length - 1] - day;
        } else {
            answers[day] = 0;
        }

        stack.push(day);
    }

    console.log(...answers);
}

// Example input
const arr = [73, 74, 75, 71, 69, 72, 76, 73];
const n = arr.length;
solve(n, arr);
