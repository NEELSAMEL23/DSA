class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

function insertNodeAtHead(head, data) {
    const newNode = new Node(data);
    newNode.next = head;
    return newNode;
}

function printList(head) {
    let current = head;
    let output = '';
    while (current) {
        output += current.data + ' ';
        current = current.next;
    }
    console.log(output.trim());
}

// Start with an empty linked list
let head = null;

// Simulated input
const inputs = [1, 2, 3];

for (let value of inputs) {
    head = insertNodeAtHead(head, value);
    printList(head);
}
