function stackOperations(operations, n) {
    const stack = [];
    const result = [];

    for (let operation of operations) {
        if (operation.startsWith("1")) {
            const [, x] = operation.split(" ");
            stack.push(parseInt(x));
        } else if (operation === "2") {
            if (stack.length > 0) {
                stack.pop();
            }
        } else if (operation === "3") {
            if (stack.length > 0) {
                result.push(stack[stack.length - 1].toString());
            } else {
                result.push("Empty!");
            }
        }
    }

    return result.join("\n");
}

const operations = ["1 15", "1 20", "2", "3", "2", "3"];
const n = 5;

const res = stackOperations(operations, n);
console.log(res);

// Output:
// 15
// Empty!
