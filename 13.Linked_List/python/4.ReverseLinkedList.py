class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Manually create the linked list
head = Node(1)
second = Node(2)
third = Node(3)
four = Node(4)
five = Node(5)

# Link the nodes
head.next = second
second.next = third
third.next = four
four.next = five

# Reverse function
def reverse(head):
    prev = None
    curr = head
    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

# Reverse the list
head = reverse(head)

# Print the reversed list
current = head
result = ""
while current is not None:
    result += str(current.data) + " -> "
    current = current.next
result += "None"

print(result)
