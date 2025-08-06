class Node{
    constructor(data){
        this.data = data
        this.next = null
    }
}

function buildLinkedList(arr){
    
    let head = new Node(arr[0])
    let current = head
    
    for(let i=1;i<arr.length;i++){
        current.next = new Node(arr[i])
        current = current.next
    }
    
    return head
}


class Solution{
    getNthFromLast(head,n) {
        
        let first = head
        let second = head
        
        let current = head
        
        for(let i=0;i<n;i++){
            first = current.next 
        }
        
        while(first !==null){
            first = first.next
            second = second.next
        }
        
        return second ? second : null
        
    }
}


function  PrintLinkedList(head){
    let res = ''
    let current = head
    
    while(current !==null){
        res += current.data + ' '
        current = current.next
    }
    
    console.log(res)
}


let arr = [1,2,3,4,5]
let Sol = new Solution()
let n = 1
let head = buildLinkedList(arr)
let newNode = Sol.getNthFromLast(head,n)
PrintLinkedList(newNode)










