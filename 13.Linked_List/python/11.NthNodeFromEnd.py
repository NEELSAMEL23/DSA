class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def getNthFromLast(head, n):
    first = head
    second = head
    
    # Move first pointer n steps ahead
    for _ in range(n):
        if first is None:
            return -1  # n is greater than the length of the list
        first = first.next
    
    # Move both pointers until first reaches the end
    while first:
        first = first.next
        second = second.next

    return second.data

# Constructing the linked list: 1 -> 2 -> 3
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

n = 1
print(getNthFromLast(head, n))  # Output: 3
