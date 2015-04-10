# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @return a list of tree node

    # Recursive Solution
    # choose every possible value from s to n to be the root
    # and recursively generate its left and right subtrees
    def generateTrees(self, n, s = 0):
        ret = []
        if s < n + 1:
            for i in range(s, n):
                for left in self.generateTrees(i, s):
                    for right in self.generateTrees(n, i + 1):
                        node = TreeNode(i + 1)
                        node.left, node.right = left, right
                        ret.append(node)
        return ret if ret else [None]