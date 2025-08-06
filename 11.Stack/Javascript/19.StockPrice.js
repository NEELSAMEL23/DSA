function calculateSpan(prices, n) {
    let span = new Array(n).fill(0);
    let stack = [];

    span[0] = 1;
    stack.push(0);

    for (let i = 1; i < n; i++) {
        while (stack.length > 0 && prices[i] >= prices[stack[stack.length - 1]]) {
            stack.pop();
        }

        if (stack.length > 0) {
            span[i] = i - stack[stack.length - 1];
        } else {
            span[i] = i + 1;
        }

        stack.push(i);
    }

    return span;
}

// Example usage:
let price = [100, 60, 70, 65, 80, 85];  // Output: [1, 1, 2, 1, 4, 5]
let n = price.length;
let result = calculateSpan(price, n);
console.log(...result);


// let prices = [10, 20, 30, 40, 50]  // Output: span = [1, 2, 3, 4, 5]
// let n = price.length;
// let result = calculateSpan(price, n);
// console.log(...result);