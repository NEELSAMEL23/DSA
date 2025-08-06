import sys
from typing import Optional

# Definition for singly-linked list.
# This class would typically be provided in a function-complete problem.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def twinSum(head: Optional[ListNode]) -> int:
    """
    Calculates the maximum twin sum in a given singly-linked list.

    A twin pair is defined by nodes at position 'i' and '(N - 1) - i',
    where 'N' is the total number of nodes (0-indexed).

    Args:
        head: The head of the singly-linked list.

    Returns:
        The maximum twin sum found in the linked list.
    """
    if not head:
        return 0  # Handle empty list case, though problem constraints might imply non-empty.

    # Step 1: Traverse the linked list and store all node values in a Python list.
    # This allows for O(1) access to nodes by their "index".
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next

    N = len(values)  # Get the total number of nodes

    # Step 2: Initialize a variable to store the maximum twin sum found so far.
    # Start with a very small number, or the sum of the first twin pair.
    max_twin_sum = 0
    if N > 0: # Ensure there's at least one pair for N > 0
        max_twin_sum = values[0] + values[N - 1] # Initialize with the first pair's sum

    # Step 3: Iterate through the first half of the list (from index 0 up to N/2 - 1).
    # For each index 'i', its twin is at index '(N - 1) - i'.
    # We only need to iterate up to N // 2 because pairs are symmetric.
    for i in range(N // 2):
        # Calculate the sum of the current twin pair
        current_twin_sum = values[i] + values[N - 1 - i]

        # Update the maximum twin sum if the current sum is greater
        if current_twin_sum > max_twin_sum:
            max_twin_sum = current_twin_sum

    return max_twin_sum

# Example Usage (for local testing purposes, not part of the function-complete solution)
# To run this, you would typically read input and build the linked list.
# For example, to test Sample Input 1:
# N = 4
# values = [5, 4, 2, 1]
# head = ListNode(values[0])
# current = head
# for i in range(1, N):
#     current.next = ListNode(values[i])
#     current = current.next
#
# result = twinSum(head)
# print(result) # Expected Output: 6

# To test Sample Input 2 (inferred):
# N = 4
# values = [4, 2, 2, 3]
# head = ListNode(values[0])
# current = head
# for i in range(1, N):
#     current.next = ListNode(values[i])
#     current = current.next
#
# result = twinSum(head)
# print(result) # Expected Output: 7
