class Node {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
}

function buildLinkedList(arr){
    if(arr.length ===0) return null
    
    let head = new Node(arr[0])
    let current = head
    
    for(let i=1;i<arr.length;i++){
        current.next = new Node(arr[i])
        current = current.next
    }
    return head
}

function deleteXAfterY(head, X, Y) {
    let current = head;

    while (current) {
        // Skip X nodes
        for (let i = 1; i < X && current != null; i++) {
            current = current.next;
        }

        // If end of list is reached
        if (current == null) break;

        // Start deleting Y nodes
        let temp = current.next;
        for (let i = 0; i < Y && temp != null; i++) {
            temp = temp.next;
        }

        // Connect current node to the (Y+1)th node
        current.next = temp;
        current = temp;
    }

    return head;
}

// Helper to print the linked list
function printList(head) {
    let result = [];
    let current = head;
    while (current) {
        result.push(current.data);
        current = current.next;
    }
    console.log(result.join(" "));
}

// Example usage:
let values = [2, 3, 2, 5, 3, 1];


let X = 3, Y = 2;
let head = buildLinkedList(values)
head = deleteXAfterY(head, X, Y);
printList(head); // Output: 2 3 2 1
