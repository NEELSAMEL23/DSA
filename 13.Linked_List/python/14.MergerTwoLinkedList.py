class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def mergeLists(A, B):
  
    dummy = Node(0)
    tail = dummy

 
    while A is not None and B is not None:
        if A.data <= B.data:
            tail.next = A
            A = A.next
        else:
            tail.next = B
            B = B.next
        tail = tail.next
    
 
    if A is not None:
        tail.next = A
    elif B is not None:
        tail.next = B

   
    return dummy.next
