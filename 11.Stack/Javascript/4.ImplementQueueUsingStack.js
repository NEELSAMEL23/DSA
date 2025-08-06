class QueueUsingStack {
    constructor() {
        this.S1 = [];
        this.S2 = [];
    }

    push(x) {
        // Move all from S1 to S2
        while (this.S1.length) {
            this.S2.push(this.S1.pop());
        }

        // Push new element to S1
        this.S1.push(x);

        // Move everything back to S1
        while (this.S2.length) {
            this.S1.push(this.S2.pop());
        }
    }

    pop() {
        if (this.S1.length) {
            this.S1.pop();
        }
    }

    front() {
        if (this.S1.length) {
            console.log(this.S1[this.S1.length - 1]);
        }
    }
}

// Hardcoded simulation
const q = new QueueUsingStack();

const queries = [
    [0, 1],
    [0, 2],
    [0, 3],
    [1],
    [2],
    [1]
];

for (const query of queries) {
    if (query[0] === 0) {
        q.push(query[1]);
    } else if (query[0] === 1) {
        q.front();
    } else if (query[0] === 2) {
        q.pop();
    }
}
