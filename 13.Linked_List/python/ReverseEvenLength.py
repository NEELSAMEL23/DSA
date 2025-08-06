class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseEvenLengthGroups(head):
    def reverse(start, end):
        prev = None
        curr = start
        while curr != end:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev  # New head of reversed part

    group_size = 1
    prev = None
    current = head

    while current:
        count = 0
        group_head = current

        # Count the actual size of the group (in case end of list is reached)
        temp = current
        while count < group_size and temp:
            temp = temp.next
            count += 1

        group_tail = temp

        if count % 2 == 0:
            # Reverse the group
            new_head = reverse(current, group_tail)

            # Connect with previous part
            if prev:
                prev.next = new_head
            else:
                head = new_head

            # Move prev to original current (now tail of reversed)
            prev = current
        else:
            # No reversal, just move prev to the last node in this group
            for _ in range(count):
                prev = current
                current = current.next

        current = group_tail
        group_size += 1

    return head

# Helper function to create a linked list
def create_linked_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

# Helper function to print linked list
def print_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(" -> ".join(map(str, result)))
