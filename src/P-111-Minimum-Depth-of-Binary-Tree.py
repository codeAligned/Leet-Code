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