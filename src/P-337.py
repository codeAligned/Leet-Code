# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # def rob(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: int
    #     """
        
    #     # Recursion with Memorization
        
    #     d = {}
        
    #     def aux(node):
    #         tmp1, tmp2 = 0, 0
    #         if not node:
    #             return 0
    #         else:
    #             # Memorization
    #             if node in d:
    #                 return d[node]
                    
    #             # Choose this node
    #             tmp1 = node.val
    #             if node.left:
    #                 tmp1 += aux(node.left.left)
    #                 tmp1 += aux(node.left.right)
    #             if node.right:
    #                 tmp1 += aux(node.right.left)
    #                 tmp1 += aux(node.right.right)
                
    #             # Skip this node
    #             tmp2 += aux(node.left)
    #             tmp2 += aux(node.right)
                
    #             d[node] = max(tmp1, tmp2)
                
    #             return max(tmp1, tmp2)
        
    #     return aux(root)
        
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        # Greedy
        
        # return (x, y) x means max val when rob the current node, y means the max val without robbing the current node
        def aux(node):
            if not node:
                return (0, 0)
            else:
                l = aux(node.left)
                r = aux(node.right)
                
                # return (max val if rob curr node, max val if not rob curr node)
                return (node.val + l[1] + r[1], max(l) + max(r))
        
        return max(aux(root))