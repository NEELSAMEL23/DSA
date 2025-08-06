class Node {
    constructor(data) {
        this.data = data
        this.next = null
    }
}

// Build linked list from array
function buildLinkedList(arr) {
    let head = new Node(arr[0])
    let current = head

    for (let i = 1; i < arr.length; i++) {
        current.next = new Node(arr[i])
        current = current.next
    }

    return head
}

class Solution {
    // Reorder nodes to group odd positions first, then even
    oddEvenReorder(head) {
        let odd = head
        let even = head.next
        let evenHead = even  // Store start of even list

        while (even && even.next) {
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next
        }

        odd.next = evenHead  // Attach even list at end of odd list
        return head
    }
}

// Print all nodes of the linked list
function PrintLinkedList(head) {
    let res = ''
    let current = head

    while (current !== null) {
        res += current.data + ' '
        current = current.next
    }

    console.log(res)
}

// Driver code
let arr = [1, 2, 3, 4, 5]
let Sol = new Solution()
let head = buildLinkedList(arr)
let newNode = Sol.oddEvenReorder(head)
PrintLinkedList(newNode)  // Output: 1 3 5 2 4
