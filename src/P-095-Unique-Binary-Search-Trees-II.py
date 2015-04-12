'''
P-095 - Unique Binary Search Trees II

Givenn, generate all structurally uniqueBST's(binary search trees)
that store values 1...n. For example,Givenn= 3, your program should
return all 5 unique BST's shown below.1         3     3      2      1
\       /     /      / \      \       3     2     1      1   3      2
/     /       \                 \     2     1         2
3 confused what"{1,#,2,3}"means?> read more on how binary tree is
serialized on OJ. The serialization of a binary tree follows a level
order traversal, where '#' signifies a path terminator where no node
exists below. Here's an example:1    / \   2   3      /     4      \
5The above binary tree is serialized as"{1,2,3,#,#,4,#,#,5}".

Tags: Tree, Dynamic Programming
'''

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