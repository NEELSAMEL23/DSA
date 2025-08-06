class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def addTwoNumbers(A, B):
    dummy = Node(0)  
    current = dummy
    carry = 0
    

    while A is not None or B is not None:
   
        x = A.data if A is not None else 0
        y = B.data if B is not None else 0
        
        total = carry + x + y
        carry = total // 10
        current.next = Node(total % 10)
        
  
        current = current.next
        
   
        if A is not None: A = A.next
        if B is not None: B = B.next
    
   
    if carry > 0:
        current.next = Node(carry)

    return dummy.next
