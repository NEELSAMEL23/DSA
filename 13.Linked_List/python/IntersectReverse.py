class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def build_linked_list(values):
    head = Node(values[0])
    current = head
    node_map = {values[0]: head}
    for val in values[1:]:
        if val in node_map:
            current.next = node_map[val]
        else:
            new_node = Node(val)
            node_map[val] = new_node
            current.next = new_node
        current = current.next
    return head, node_map

def get_intersection_node(headA, headB):
    # Count lengths
    def get_length(head):
        count = 0
        while head:
            count += 1
            head = head.next
        return count

    lenA = get_length(headA)
    lenB = get_length(headB)

    # Align both pointers
    while lenA > lenB:
        headA = headA.next
        lenA -= 1
    while lenB > lenA:
        headB = headB.next
        lenB -= 1

    # Find intersection
    while headA and headB:
        if headA is headB:
            return headA
        headA = headA.next
        headB = headB.next
    return None

def reverse_from_node(node):
    prev = None
    while node:
        next_node = node.next
        node.next = prev
        prev = node
        node = next_node
    return prev

def print_linked_list(head):
    result = []
    while head:
        result.append(str(head.data))
        head = head.next
    print(" ".join(result))

# Input reading
n, m = map(int, input().split())
listA = list(map(int, input().split()))
listB = list(map(int, input().split()))

# Build list A
headA, node_map = build_linked_list(listA)

# Build list B (reuse intersection nodes from listA)
headB = Node(listB[0])
curr = headB
for val in listB[1:]:
    if val in node_map:
        curr.next = node_map[val]
        break
    else:
        curr.next = Node(val)
        curr = curr.next

# Find intersection node
intersect_node = get_intersection_node(headA, headB)

# Reverse from intersection node
reversed_head = reverse_from_node(intersect_node)

# Print output
print_linked_list(reversed_head)
