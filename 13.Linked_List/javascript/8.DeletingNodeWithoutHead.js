class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

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

function deleteByValueWithoutHead(head, value) {
    let current = head;

    while (current !== null) {
        if (current.data === value && current.next !== null) {
            current.data = current.next.data;
            current.next = current.next.next;
            return;
        }
        current = current.next;
    }
    // If it's the tail or not found, we can't delete this way
}

function printList(head) {
    let current = head;
    let res = '';
    while (current !== null) {
        res += current.data + ' ';
        current = current.next;
    }
    console.log(res.trim());
}

let arr = [1, 2, 3]
let head = buildLinkedList(arr);
let valueToDelete = 2;
deleteByValueWithoutHead(head, valueToDelete);
printList(head);  // Output: 1 3
