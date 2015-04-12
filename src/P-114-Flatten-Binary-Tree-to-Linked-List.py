'''
P-114 - Flatten Binary Tree to Linked List

Given a binary tree, flatten it to a linked list in-place. For
example,Given1          / \         2   5        / \   \       3   4
6 click to show hints. If you notice carefully in the flattened tree,
each node's right child points to the next node of a pre-order
traversal.

Tags: Tree, Depth-first Search
'''

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if not root:
            return
        stack, prev = [root, ], None
        while stack:
            node = stack.pop()
            if prev != None:
                prev.right = node
                prev.left = None
            prev = node
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(5)
t.left.left = TreeNode(3)
t.left.right = TreeNode(4)
t.right.right = TreeNode(6)
t.right.right.left = TreeNode(7)

s = Solution()
s.flatten(t)

ptr = t
while ptr:
    print ptr.val, '->',
    ptr = ptr.right
