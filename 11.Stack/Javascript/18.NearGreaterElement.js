function nearestGreaterElement(arr, n) {
    let stack = [];
    let result = [];

    for (let i = 0; i < n; i++) {
        while (stack.length > 0 && stack[stack.length - 1] <= arr[i]) {
            stack.pop();
        }

        if (stack.length > 0) {
            result.push(stack[stack.length - 1]);
        } else {
            result.push(-1);
        }

        stack.push(arr[i]);
    }

    return result;
}

let n = 8;
let arr = [39, 27, 11, 4, 24, 32, 32, 1];

let res = nearestGreaterElement(arr, n);
console.log(res);
