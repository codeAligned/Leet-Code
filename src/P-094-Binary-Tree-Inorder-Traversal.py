# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def recursive(self, node):
        if node.left:
            self.recursive(node.left)
        self.ret.append(node.val)
        if node.right:
            self.recursive(node.right)

    def iterative(self, root):
        stack = [(root, False), ]
        while stack:
            node, visited = stack.pop()
            if visited:
                self.ret.append(node.val)
            else:
                if node.right:
                    stack.append((node.right, False))
                stack.append((node, True))
                if node.left:
                    stack.append((node.left, False))

    def inorderTraversal(self, root):
        self.ret = []
        if root:
            #self.recursive(root)
            self.iterative(root)
        return self.ret