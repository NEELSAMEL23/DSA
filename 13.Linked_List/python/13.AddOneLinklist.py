class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def addOne(head):

    head = reverse(head)


    current = head
    carry = 1

    while current is not None:
        current.data += carry
        if current.data < 10:
            carry = 0  
            break
        else:
            current.data = 0
            carry = 1


        if current.next is None and carry > 0:
            current.next = Node(1)  
            carry = 0
        current = current.next


    head = reverse(head)

    return head

def reverse(head):
    prev = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev
