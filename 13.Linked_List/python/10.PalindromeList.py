class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def isPalindrome(head):
    values = []
    
    # Traverse the linked list and collect node values
    current = head
    while current:
        values.append(current.data)
        current = current.next
    
    # Check if list of values is equal to its reverse
    return values == values[::-1]

def printLinkedList(head):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()

# 🔸 Hardcoded Palindrome List: 1 -> 2 -> 3 -> 2 -> 1
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(2)
node5 = ListNode(1)

# Linking the nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

head = node1

# Print list and check palindrome
printLinkedList(head)  # Output: 1 2 3 2 1
print("Is Palindrome?", isPalindrome(head))  # Output: True
