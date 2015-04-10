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
    def connect(self, root):
        if not root:
            return
        while root.left:
            curr = root
            while curr:
                curr.left.next = curr.right
                # We can do this because the we have built the next pointer
                # for the upper level
                if curr.next:
                    curr.right.next = curr.next.left
                curr = curr.next
            root = root.left