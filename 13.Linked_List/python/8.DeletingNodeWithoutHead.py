class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteNode(node):
    # Copy next node's data to current node and bypass the next node
    if node and node.next:
        node.val = node.next.val
        node.next = node.next.next

def printLinkedList(head):
    current = head
    while current:
        print(current.val, end=" ")
        current = current.next
    print()

# Hardcoded linked list: 1 -> 2 -> 3
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)

# Link nodes
node1.next = node2
node2.next = node3

# Delete node with value 2 (simulate being given only the node2 reference)
deleteNode(node2)

# Print updated list: should be 1 -> 3
printLinkedList(node1)
