# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean

    # Recursive DFS solution
    def hasPathSum(self, root, sum):
        if not root:
            return False
        if not root.left and not root.right:
            return sum == root.val
        found = False
        if root.left:
            found |= self.hasPathSum(root.left, sum - root.val)
        if root.right:
            found |= self.hasPathSum(root.right, sum - root.val)
        return found

s = Solution()
t = TreeNode(-2)
t.right = TreeNode(-3)

print s.hasPathSum(t, -5)