class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insertNodeAtHead(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node

def printList(head):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()

# Start with an empty linked list
head = None

# Simulated input
inputs = [1, 2, 3]

for value in inputs:
    head = insertNodeAtHead(head, value)
    printList(head)
