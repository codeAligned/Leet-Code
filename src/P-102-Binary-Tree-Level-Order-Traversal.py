'''
P-102 - Binary Tree Level Order Traversal

Given a binary tree, return thelevel ordertraversal of its nodes'
values. (ie, from left to right, level by level). For example:Given
binary tree{3,9,20,#,#,15,7},3     / \    9  20      /  \     15   7
return its level order traversal as:[    [3],    [9,20],    [15,7]  ]
confused what"{1,#,2,3}"means?> read more on how binary tree is
serialized on OJ. The serialization of a binary tree follows a level
order traversal, where '#' signifies a path terminator where no node
exists below. Here's an example:1    / \   2   3      /     4      \
5The above binary tree is serialized as"{1,2,3,#,#,4,#,#,5}".

Tags: Tree, Breadth-first Search
'''

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