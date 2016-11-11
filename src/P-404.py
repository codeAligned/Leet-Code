# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        LEFT = 0
        RIGHT = 1
        
        def visit(node, d):
            s = 0
            if not node:
                return 0
            # Left leaf?
            if not node.left and not node.right and d == LEFT:
                return node.val
            else:
                return visit(node.left, LEFT) + visit(node.right, RIGHT)
                
        # Assume root is not left leaf
        return visit(root, 1) 