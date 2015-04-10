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