from collections import defaultdict
import sys
sys.setrecursionlimit(1 << 25)

n = int(input())
s = input()

# Create doubly linked list pointers
left = defaultdict(int)
right = defaultdict(int)

# 0 is initially present
# Set initial pointers
left[0] = -1
right[0] = -1

last = 0  # Pointer to the most recently inserted value

for i in range(1, n + 1):
    if s[i - 1] == 'L':
        prev = left[last]
        # Link new node i between prev and last
        if prev != -1:
            right[prev] = i
        left[i] = prev
        right[i] = last
        left[last] = i
    else:
        nxt = right[last]
        if nxt != -1:
            left[nxt] = i
        right[i] = nxt
        left[i] = last
        right[last] = i
    last = i  # Update last to current inserted

# Traverse to leftmost node
curr = 0
while left[curr] != -1:
    curr = left[curr]

# Print result from leftmost to rightmost
res = []
while curr != -1:
    res.append(str(curr))
    curr = right[curr]

print(" ".join(res))
