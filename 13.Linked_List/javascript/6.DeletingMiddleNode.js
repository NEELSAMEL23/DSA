// Node class definition
class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

// Function to build a linked list from an array
function buildLinkedList(arr) {
    if (arr.length === 0) return null;

    let head = new Node(arr[0]);
    let current = head;

    for (let i = 1; i < arr.length; i++) {
        current.next = new Node(arr[i]);
        current = current.next;
    }

    return head;
}

// Function to remove the middle node
function removeMiddleNode(head, n) {
    if (n === 1) return null; // Only one node, remove it

    let middle = Math.floor(n / 2); // 0-based index

    if (middle === 0) return head.next; // If only two nodes

    let current = head;
    for (let i = 0; i < middle - 1; i++) {
        current = current.next;
    }

    if (current.next) {
        current.next = current.next.next;
    }

    return head;
}

// Function to print linked list
function printList(head) {
    let current = head;
    let result = [];
    while (current) {
        result.push(current.data);
        current = current.next;
    }
    console.log(result.join(" "));
}

// ----------- INPUT -----------
const inputs = [3, 1, 3, 4, 5, 5, 2];
const n = inputs.length;

// ----------- BUILD, PROCESS, PRINT -----------
let head = buildLinkedList(inputs);
let newHead = removeMiddleNode(head, n);
printList(newHead);  // Output: 3 1 3 5 5 2
