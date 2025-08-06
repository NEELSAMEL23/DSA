function maximizeTop(N, K, stack) {
    if (N === 0) {
        return -1;
    }

    if (K === 0) {
        return stack[0];
    }

    if (K === 1) {
        if (N >= 2) {
            return stack[1];
        } else {
            return -1;
        }
    }

    if (K > N) {
        return Math.max(...stack);
    }

    if (K === N) {
        return Math.max(...stack.slice(0, K - 1));
    }

    // General case
    return Math.max(Math.max(...stack.slice(0, K - 1)), stack[K]);
}

// Hardcoded input
const N = 6;
const K = 3;
const stack = [1, 2, 4, 3, 3, 5];

const result = maximizeTop(N, K, stack);
console.log(result);
