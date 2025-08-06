class Node {
    constructor(data) {
        this.data = data
        this.next = null
    }
}

function buildLinkedList(arr) {
    if (arr.length === 0) return null

    let head = new Node(arr[0])
    let current = head

    for (let i = 1; i < arr.length; i++) {
        current.next = new Node(arr[i])
        current = current.next
    }

    return head
}

class Solution {
    reverseNodes(head) {
        let current = head
        let prev = null

        while (current !== null) {
            let next = current.next
            current.next = prev
            prev = current
            current = next
        }

        return prev
    }


}

function PrintList(head) {
    let res = ''
    let current = head
    while (current !== null) {
        res += current.data + ' '
        current = current.next
    }

    console.log(res)
}

let arr = [1, 2, 3, 4, 5]
let n = 3
let Sol = new Solution()

let head = buildLinkedList(arr)
let newHead = Sol.reverseNodes(head)
PrintList(newHead)
