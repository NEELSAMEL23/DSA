# Define the Node class (already given)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Manually create the linked list
head = Node(10)
second = Node(20)
third = Node(30)

# Link the nodes
head.next = second
second.next = third

# Count the number of nodes
def count_nodes(head):
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    return count

# Call the function and display the count
print("Number of nodes:", count_nodes(head))
