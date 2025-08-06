class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None

def deleteYAfterX(head, N, X, Y):
    current = head
    
    while current:
       
        for i in range(1, X):
            if current is None:
                return head
            current = current.next

        if current is None:
            return head

        
        temp = current.next
        for i in range(Y):
            if temp is None:
                break
            temp = temp.next

       
        current.next = temp

        current = temp

    return head
