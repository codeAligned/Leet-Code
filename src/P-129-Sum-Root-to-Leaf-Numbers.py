'''
P-129 - Sum Root to Leaf Numbers

Given a binary tree containing digits from0-9only, each root-to-leaf
path could represent a number. An example is the root-to-leaf
path1->2->3which represents the number123. Find the total sum of all
root-to-leaf numbers. For example,1     / \    2   3 The root-to-leaf
path1->2represents the number12.The root-to-leaf path1->3represents
the number13. Return the sum = 12 + 13 =25.

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
    def dfs(self, node, num):
        if not node.left and not node.right:
            self.ret.append(num * 10 + node.val)
        if node.left:
            self.dfs(node.left, num * 10 + node.val)
        if node.right:
            self.dfs(node.right, num * 10 + node.val)

    def sumNumbers(self, root):
        self.ret = []
        if not root:
            return 0
        self.dfs(root, 0)
        return sum(self.ret)

t = TreeNode(1)
t.left = TreeNode(2)
t.left.left = TreeNode(2)
t.left.right = TreeNode(4)
t.right = TreeNode(3)

s = Solution()
print s.sumNumbers(t)