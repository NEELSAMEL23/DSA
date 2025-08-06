// Define the Node class
class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

// Manually create the linked list
const head = new Node(10);
const second = new Node(20);
const third = new Node(30);

// Link the nodes
head.next = second;
second.next = third;

// Function to count the number of nodes
function countNodes(head) {
    let count = 0;
    let current = head;
    while (current !== null) {
        count++;
        current = current.next;
    }
    return count;
}

// Call the function and display the count
console.log("Number of nodes:", countNodes(head));
