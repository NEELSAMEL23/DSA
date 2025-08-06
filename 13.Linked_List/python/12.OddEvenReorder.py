class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def oddEvenList(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head

    odd_current = head          
    even_head = head.next       
    even_current = head.next    

    while even_current and even_current.next:
        odd_current.next = even_current.next
        odd_current = odd_current.next

        even_current.next = odd_current.next
        even_current = even_current.next

    odd_current.next = even_head

    return head

if __name__ == "__main__":
    def create_linked_list(arr):
        if not arr:
            return None
        head = ListNode(arr[0])
        current = head
        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def print_linked_list(head):
        current = head
        nodes = []
        while current:
            nodes.append(str(current.val))
            current = current.next
        print(" -> ".join(nodes) if nodes else "Empty List")

    print("Enter numbers for the linked list, separated by spaces (e.g., 1 2 3 4 5):")
    try:
        input_str = input()
        
        num_strings = input_str.split()
        if not num_strings:
            print("No numbers entered. Creating an empty list.")
            input_list_values = []
        else:
            input_list_values = [int(s) for s in num_strings]

        initial_list_head = create_linked_list(input_list_values)

        print("\nOriginal List:")
        print_linked_list(initial_list_head)

        reordered_list_head = oddEvenList(initial_list_head)

        print("\nReordered List (Odd indices first, then Even):")
        print_linked_list(reordered_list_head)

    except ValueError:
        print("Invalid input. Please ensure you enter integers separated by spaces.")
    except Exception as e:
        print(f"An error occurred: {e}")
