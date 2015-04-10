# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer

    def aux(self, node):
        if not node:
            return 0
        l = max(0, self.aux(node.left))
        r = max(0, self.aux(node.right))
        self.max = max(self.max, l + r + node.val)
        return node.val + max(l, r)

    def maxPathSum(self, root):
        self.max = -2**31
        self.aux(root)
        return self.max