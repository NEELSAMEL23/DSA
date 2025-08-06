function stack_operations(operations, n) {
    let stack = [];
    let result = [];

    for (let operation of operations) {
        if (operation[0] === "1") {
            if (stack.length > 0) {
                result.push(stack.pop().toString());
            } else {
                result.push("No Food");
            }
        } else if (operation[0] === "2") {
            const [, x] = operation.split(" ");
            stack.push(parseInt(x));
        }
    }

    return result.join("\n");
}

const operations = ["1", "2 5", "2 7", "2 9", "1", "1"];
const n = 5;

const res = stack_operations(operations, n);
console.log(res);

// Output:
// No Food
// 9
// 7
