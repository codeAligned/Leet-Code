'''
P-111 - Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth. The minimum depth is the
number of nodes along the shortest path from the root node down to the
nearest leaf node.

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
    def __init__(self):
        self.result = []

    # Recursive DFS solution
    def minDepth(self, root, depth = 1):
        if root == None:
            return 0
        if not root.left and not root.right:
            self.result.append(depth)
        if root.left:
            self.minDepth(root.left, depth + 1)
        if root.right:
            self.minDepth(root.right, depth + 1)
        return min(self.result)

    # Level-order traversal would be faster

s = Solution()

t = TreeNode(-2)
#t.right = TreeNode(-3)

print s.minDepth(t)