'''
P-110 - Balanced Binary Tree

Given a binary tree, determine if it is height-balanced. For this
problem, a height-balanced binary tree is defined as a binary tree in
which the depth of the two subtrees ofeverynode never differ by more
than 1.

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
    # @return a boolean

    # DFS-based Solution
    def dfs(self, node):
        l_height = r_height = 0
        l_flag = r_flag = True
        if node.left:
            l_height, l_flag = self.dfs(node.left)
        if node.right:
            r_height, r_flag = self.dfs(node.right)
        return max(l_height, r_height) + 1, l_flag and r_flag and max(l_height, r_height) - min(l_height, r_height) <= 1

    def isBalanced(self, root):
        if root == None:
            return True
        return self.dfs(root)[1]

s = Solution()

t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(2)
t.left.left = TreeNode(3)
t.left.right = TreeNode(3)
t.right.left = TreeNode(3)
t.right.right = TreeNode(3)
t.left.left.left = TreeNode(4)
t.left.right.left = TreeNode(4)
t.right.left.left = TreeNode(4)
#t.right.right.left = TreeNode(4)
t.left.left.right = TreeNode(4)
t.left.right.right = TreeNode(4)
t.right.left.right = TreeNode(4)
#t.right.right.right = TreeNode(4)
t.left.left.left.left = TreeNode(5)
t.left.left.left.right = TreeNode(5)

print s.isBalanced(t)