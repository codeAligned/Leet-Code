'''
P-094 - Binary Tree Inorder Traversal

Given a binary tree, return theinordertraversal of its nodes' values.
For example:Given binary tree{1,#,2,3},1      \       2      /     3
return[1,3,2]. Note:Recursive solution is trivial, could you do it
iteratively? confused what"{1,#,2,3}"means?> read more on how binary
tree is serialized on OJ. The serialization of a binary tree follows a
level order traversal, where '#' signifies a path terminator where no
node exists below. Here's an example:1    / \   2   3      /     4
\       5The above binary tree is serialized as"{1,2,3,#,#,4,#,#,5}".

Tags: Tree, Hash Table, Stack
'''

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