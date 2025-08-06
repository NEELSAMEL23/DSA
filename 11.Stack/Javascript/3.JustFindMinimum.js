function justFindMinimum(operations) {
    let mainStack = [];
    let minStack = [];
    let res = [];

    for (let operation of operations) {
        const [op, value] = operation.split(' ');

        if (op === 'PUSH') {
            const x = parseInt(value);
            mainStack.push(x);
            if (minStack.length === 0 || x <= minStack[minStack.length - 1]) {
                minStack.push(x);
            }
        } else if (op === 'POP') {
            if (mainStack.length > 0) {
                const popped = mainStack.pop();
                if (popped === minStack[minStack.length - 1]) {
                    minStack.pop();
                }
            } else {
                res.push('Empty!');
            }
        } else if (op === 'MIN') {
            if (mainStack.length > 0) {
                res.push(minStack[minStack.length - 1]);
            } else {
                res.push('Empty!');
            }
        }
    }

    console.log(res);
}

const operations = [
    "PUSH 5",
    "PUSH 7",
    "PUSH 3",
    "PUSH 8",
    "PUSH 10",
    "MIN",
    "POP",
    "POP",
    "MIN",
    "POP",
    "MIN"
];

justFindMinimum(operations);
