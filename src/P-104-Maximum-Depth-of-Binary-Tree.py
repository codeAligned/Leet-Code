'''
P-104 - Maximum Depth of Binary Tree

Given a binary tree, find its maximum depth. The maximum depth is the
number of nodes along the longest path from the root node down to the
farthest leaf node.

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
    # @return an integer
    def dfs(self, node, level):
        if node:
            self.dfs(node.left, level + 1)
            self.dfs(node.right, level + 1)
        else:
            self.ret.append(level - 1)  # or level
    
    def maxDepth(self, root):
        self.ret = [0]
        self.dfs(root, 1)               # or 0
        return max(self.ret)

s = Solution()

t = TreeNode(0)
t.left = TreeNode(1)
t.right = TreeNode(2)
t.right.left = TreeNode(3)
t.right.right = TreeNode(4)
t.right.left.right = TreeNode(5)

print s.maxDepth(t)