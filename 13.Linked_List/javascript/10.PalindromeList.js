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
    isPalindrome(head) {
        let values = []
        
        let current = head
        
        while(current !== null){
            values.push(current.data)
            current = current.next
        }
        
        let reverse = [...values].reverse()
        
        return values.every((val,indx)=>val===reverse[indx])
        
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


let arr = [1,2,1]
let Sol = new Solution()

let head = buildLinkedList(arr)
let isPalin = Sol.isPalindrome(head)
console.log(`is Palindrome: ${isPalin}`)
PrintLinkedList(head)










