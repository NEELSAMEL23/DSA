class Node{
    constructor(data){
        this.data = data
        this.next = null
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


function deleteNodeAtPosition(head,postion){
    
    let current = head
    
    for(let i=0;i<postion-1;i++){
        current = current.next
    }
    
    if(current.next){
        current.next = current.next.next
    }
    
    return head
}


function printList(head){
    let current = head 
    let res = ''
    while(current!==null){
        res += current.data + ' '
        current = current.next
    }
    
    console.log(res)
}

let inputs = [1,2,3,4,5]
let postion = 2

let head = buildLinkedList(inputs)
let newHead = deleteNodeAtPosition(head,postion)
printList(newHead)

