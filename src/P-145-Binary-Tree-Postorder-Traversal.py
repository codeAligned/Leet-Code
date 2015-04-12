'''
P-145 - Binary Tree Postorder Traversal

Given a binary tree, return thepostordertraversal of its nodes'
values. For example:Given binary tree{1,#,2,3},1      \       2      /
3 return[3,2,1]. Note:Recursive solution is trivial, could you do it
iteratively?

Tags: Tree, Stack
'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def recursive(self, node):
        if not node:
            return
        self.recursive(node.left)
        self.recursive(node.right)
        self.ret.append(node.val)

    def iterative(self, root):
        stack = [(root, False), ]
        while stack:
            node, visited = stack.pop()
            if visited:
                self.ret.append(node.val)
            else:
                stack.append((node, True))
                if node.right:
                    stack.append((node.right, False))
                if node.left:
                    stack.append((node.left, False))

    def preorderTraversal(self, root):
        self.ret = []
        self.recursive(root)
        return self.ret