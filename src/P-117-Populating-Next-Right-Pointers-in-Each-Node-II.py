# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing

    # Level-order traversal
    def connect(self, root):
        # Current node of current level
        curr = root
        # Head of the next level
        head = None
        # The leading node on the next level
        prev = None
        while curr:
            # Iterate on the current level
            while curr:
                # Left child
                if curr.left:
                    if prev:
                        prev.next = curr.left
                    else:
                        head = curr.left
                    prev = curr.left
                # Right child
                if curr.right:
                    if prev:
                        prev.next = curr.right
                    else:
                        head = curr.right
                    prev = curr.right
                # Move to next node
                curr = curr.next
            # Move to next level
            curr = head
            head = prev = None