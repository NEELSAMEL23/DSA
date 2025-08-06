class Node:
    def __init__(self, data): 
        self.data = data 
        self.next = None

class Solution:
    def hasCycle(self, head):
        slow = head
        fast = head
        
        while fast is not None and fast.next is not None:
            slow = slow.next          
            fast = fast.next.next    
            
            if slow == fast:
                return True
        
        return False

def reverse(A):
    prev = None
    current = A
    while current is not None:
        nextNode = current.next
        current.next = prev
        prev = current
        current = nextNode
    return prev
