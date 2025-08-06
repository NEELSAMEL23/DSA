function isValidStackSequence(pushed, popped) {
    const stack = [];
    let j = 0;

    for (let num of pushed) {
        stack.push(num);

        while (stack.length && stack[stack.length - 1] === popped[j]) {
            stack.pop();
            j++;
        }
    }

    return stack.length === 0 ? "Yes" : "No";
}

const n = 5;
const pushed = [1, 2, 3, 4, 5];
const popped = [5, 4, 3, 2, 1];
const result = isValidStackSequence(pushed, popped);
console.log(result);
