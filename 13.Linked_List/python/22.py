class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head: ListNode) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    while prev.next and prev.next.next:

        first = prev.next
        second = prev.next.next
        
        prev.next = second
        first.next = second.next
        second.next = first
       
        prev = first
    
    return dummy.next


def create_linked_list(arr):
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    head = create_linked_list(arr)
    new_head = swapPairs(head)
    print(*linked_list_to_list(new_head))
