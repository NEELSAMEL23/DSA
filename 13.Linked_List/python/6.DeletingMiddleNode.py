class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to build a linked list from a list
def build_linked_list(arr):
    if not arr:
        return None

    head = Node(arr[0])
    current = head

    for val in arr[1:]:
        current.next = Node(val)
        current = current.next

    return head

# Function to remove the middle node
def remove_middle_node(head, n):
    if n == 1:
        return None  # Only one node

    middle = n // 2  # 0-based middle index

    if middle == 0:
        return head.next  # Remove the first node in 2-element list

    current = head
    for _ in range(middle - 1):
        current = current.next

    if current.next:
        current.next = current.next.next

    return head

# Function to print the linked list
def print_list(head):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.next
    print()

# ----------- INPUT -----------
inputs = [3, 1, 3, 4, 5, 5, 2]
n = len(inputs)

# ----------- BUILD, PROCESS, PRINT -----------
head = build_linked_list(inputs)
new_head = remove_middle_node(head, n)
print_list(new_head)  # Output: 3 1 3 5 5 2
