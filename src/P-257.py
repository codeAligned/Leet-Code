# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        ret_list = []
        temp = []
        
        def aux(node, l):
            l.append(node.val)
            if not node.left and not node.right:
                temp.append(l[:])
            if node.left:
                aux(node.left, l)
            if node.right:
                aux(node.right, l)
            l.pop()
            
        if root:
            aux(root, [])
            
        for path in temp:
            s = ''
            for i, v in enumerate(path):
                s += str(v)
                if i != len(path) - 1:
                    s += '->'
            ret_list.append(s)
                
        return ret_list