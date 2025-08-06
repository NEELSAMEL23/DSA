# Definition of Linked List Node
# class Node: 
#     def __init__(self, data): 
#         self.data = data 
#         self.next = None

class Solution:
    def insertNodeAtaPosition(self, head, data, position):
        new_node = Node(data)
        
        # Case: Insert at the beginning (position 0)
        if position == 0:
            new_node.next = head
            return new_node
        
        # Traverse to the node just before the insertion point
        current = head
        count = 0
        
        while current is not None and count < position - 1:
            current = current.next
            count += 1

        # Insert the new node
        new_node.next = current.next
        current.next = new_node
        
        return head
