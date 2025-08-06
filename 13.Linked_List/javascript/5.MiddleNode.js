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

class Solution {
    MiddleNode(head, n) {
        let middle = Math.floor(n / 2);
        let current = head;

        for (let i = 0; i < middle; i++) {
            current = current.next;
        }

        return current; // return just the middle node
    }
}

function PrintMiddleNode(node) {
    if (node !== null) {
        console.log(node.data);
    } else {
        console.log("List is empty");
    }
}

let arr = [1, 2, 3];
let n = arr.length;

let Sol = new Solution();
let head = buildLinkedList(arr);
let middleNode = Sol.MiddleNode(head, n);
PrintMiddleNode(middleNode);
