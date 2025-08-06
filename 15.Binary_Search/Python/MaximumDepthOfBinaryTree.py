"""
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
"""

def maxDepth(root):
    if root is None:
        return 0
    
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    
    return max(left_depth, right_depth) + 1
