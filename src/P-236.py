# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
       
        if root in (None, p, q):
            return root
        
        children = [self.lowestCommonAncestor(node, p, q) for node in (root.left, root.right)]
        
        return root if all(children) else max(children)