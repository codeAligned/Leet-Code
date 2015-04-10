# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def dfs(self, node, level):
        if node:
            if len(self.ret) <= level:
                self.ret.append([])
            self.ret[level].append(node.val)
            self.dfs(node.left, level + 1)
            self.dfs(node.right, level + 1)

    def levelOrder(self, root):
        self.ret = []
        if not root:
            return self.ret
        self.dfs(root, 0)
        return self.ret

s = Solution()

t = TreeNode(0)
t.left = TreeNode(1)
t.right = TreeNode(2)
t.right.left = TreeNode(3)
t.right.right = TreeNode(4)

for item in s.levelOrder(t):
    print item