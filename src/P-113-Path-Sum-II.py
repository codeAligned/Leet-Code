# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers

    # Recursive DFS solution
    def dfs(self, node, l = []):
        if not node.left and not node.right:
            if sum(l) + node.val == self.sum:
                return [l + [node.val]]
            else:
                return []
        ret = []
        if node.left:
            ret += self.dfs(node.left, l + [node.val, ])
        if node.right:
            ret += self.dfs(node.right, l + [node.val, ])
        return ret

    def pathSum(self, root, sum):
        if not root:
            return [
        self.sum = sum
        ret = self.dfs(root)
        return filter(lambda x: len(x) > 0, ret)

s = Solution()
t = TreeNode(5)
t.left = TreeNode(4) 
t.right = TreeNode(8) 
t.left.left = TreeNode(11)
t.left.left.left = TreeNode(7) 
t.left.left.right = TreeNode(2) 
t.right.left = TreeNode(13)
t.right.right = TreeNode(4) 
t.right.right.left = TreeNode(5) 
t.right.right.right = TreeNode(1)

print s.pathSum(t, 22)