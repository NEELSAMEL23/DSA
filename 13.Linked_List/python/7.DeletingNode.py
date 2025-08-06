class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteNodeAtPosition(head, position):
    if not head:
        return None
    if position == 0:
        return head.next

    current = head
    count = 0

    while current and count < position - 1:
        current = current.next
        count += 1

    if current and current.next:
        current.next = current.next.next

    return head

def print_linked_list(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()

# --- Hardcoded Linked List ---
# Input: [20, 6, 2, 19, 7, 4, 15, 9]
node1 = ListNode(20)
node2 = ListNode(6)
node3 = ListNode(2)
node4 = ListNode(19)
node5 = ListNode(7)
node6 = ListNode(4)
node7 = ListNode(15)
node8 = ListNode(9)

# Manually linking the nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8

# Head of the list
head = node1

# Hardcoded position to delete
position = 3  # delete value 19

# Perform deletion
head = deleteNodeAtPosition(head, position)

# Print updated list
print_linked_list(head)
