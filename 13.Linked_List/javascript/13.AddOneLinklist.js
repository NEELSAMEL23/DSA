class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

// Convert array to linked list
function buildLinkedList(arr) {
    let head = new Node(arr[0]);
    let current = head;

    for (let i = 1; i < arr.length; i++) {
        current.next = new Node(arr[i]);
        current = current.next;
    }

    return head;
}

class Solution {
    // Add one to number represented by linked list
    addOne(head) {
        head = this.reverse(head); // Reverse to start from least significant digit
        let current = head;
        let carry = 1;

        // Traverse and add carry
        while (current !== null) {
            current.data += carry;

            if (current.data < 10) {
                carry = 0; // No carry, done
                break;
            } else {
                current.data = 0; // Reset to 0 and carry over
                carry = 1;
            }

            // If at end and still carry, add new node
            if (current.next === null && carry > 0) {
                current.next = new Node(1);
                carry = 0;
            }

            current = current.next;
        }

        return this.reverse(head); // Reverse again to restore original order
    }

    // Reverse linked list
    reverse(head) {
        let prev = null;
        let current = head;

        while (current !== null) {
            let nextNode = current.next;
            current.next = prev;
            prev = current;
            current = nextNode;
        }

        return prev;
    }
}

// Print linked list
function PrintLinkedList(head) {
    let res = '';
    let current = head;

    while (current !== null) {
        res += current.data + ' ';
        current = current.next;
    }

    console.log(res);
}

// Test case
let arr = [1, 9, 9];
let Sol = new Solution();
let head = buildLinkedList(arr);
let newNode = Sol.addOne(head);
PrintLinkedList(newNode); // Output: 2 0 0
