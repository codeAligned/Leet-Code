# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean

    # Recursive solution
    def aux(self, left, right):
        # If any of the left or right is None
        # check if the other one is None also.
        if not left or not right:
            return left == right
        # left and right need to have same value
        # the left of left should be the same with the right of the right
        # the right of left should be the same with the left of the right
        return left.val == right.val and                \
                self.aux(left.left, right.right) and    \
                self.aux(left.right, right.left)

    def isSymmetric(self, root):
        return not root or self.aux(root.left, root.right)