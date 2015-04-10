# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, modify the binary tree in-place instead.

    # In-order traversal
    def traverse(self, node):
        if not node:
            return
        self.traverse(node.left)
        # Compare the current elements with the previous one
        # and find out the first and second node which violate the sorted
        # order of in-order traversal
        if not self.first and self.prev.val >= node.val:
            self.first = self.prev
        if self.first and self.prev.val >= node.val:
            self.second = node
        self.prev = node
        self.traverse(node.right)

    def recoverTree(self, root):
        from sys import maxint
        self.first = self.second = None
        self.prev = TreeNode(-maxint)
        self.traverse(root)
        # Swap the value of the two nodes
        self.first.val, self.second.val = self.second.val, self.first.val