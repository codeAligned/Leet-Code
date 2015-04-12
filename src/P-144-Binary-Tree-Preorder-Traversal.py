'''
P-144 - Binary Tree Preorder Traversal

Given a binary tree, return thepreordertraversal of its nodes' values.
For example:Given binary tree{1,#,2,3},1      \       2      /     3
return[1,2,3]. Note:Recursive solution is trivial, could you do it
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
        self.ret.append(node.val)
        self.recursive(node.left)
        self.recursive(node.right)

    def iterative(self, root):
        if not root:
            return
        stack = [root, ]
        while stack:
            node = stack.pop()
            if not node:
                continue
            self.ret.append(node.val)
            stack.append(node.left)
            stack.append(node.right)

    def preorderTraversal(self, root):
        self.ret = []
        self.recursive(root)
        return self.ret