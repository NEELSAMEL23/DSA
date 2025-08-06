function signalRanges(heights) {
    const n = heights.length;
    const stack = [];
    const res = [];

    for (let i = 0; i < n; i++) {
        while (stack.length > 0 && heights[stack[stack.length - 1]] <= heights[i]) {
            stack.pop();
        }

        if (stack.length > 0) {
            res.push(i - stack[stack.length - 1]);
        } else {
            res.push(i + 1);
        }

        stack.push(i);
    }

    return res;
}

// Single hardcoded input
const heights = [100, 80, 60, 70, 60, 75, 85];
const result = signalRanges(heights);
console.log(result.join(' '));
