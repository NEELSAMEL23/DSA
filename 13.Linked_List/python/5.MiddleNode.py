# Definition of Linked List Node
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None

class Solution:
    def middleNode(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None

# Sample usage
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

sol = Solution()
print("Middle element:", sol.middleNode(head))
