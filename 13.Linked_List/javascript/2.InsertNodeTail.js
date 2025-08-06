class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}

class Solution {
  insertNodeAtTail(head, data) {
    const newNode = new Node(data);

    if (head === null) {
      return newNode;
    }

    let current = head;
    while (current.next !== null) {
      current = current.next;
    }

    current.next = newNode;
    return head;
  }
} 

function printList(head) {
  let current = head;
  let result = '';
  while (current !== null) {
    result += current.data + ' ';
    current = current.next;
  }
  console.log(result.trim());
}

// Simulated input
const inputs = [1, 2, 3];
let head = null;

const sol = new Solution();

for (let value of inputs) {
  head = sol.insertNodeAtTail(head, value);
  printList(head);
}
