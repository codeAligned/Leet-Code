'''
P-103 - Binary Tree Zigzag Level Order Traversal

Given a binary tree, return thezigzag level ordertraversal of its
nodes' values. (ie, from left to right, then right to left for the
next level and alternate between). For example:Given binary
tree{3,9,20,#,#,15,7},3     / \    9  20      /  \     15   7 return
its zigzag level order traversal as:[    [3],    [20,9],    [15,7]  ]
confused what"{1,#,2,3}"means?> read more on how binary tree is
serialized on OJ. The serialization of a binary tree follows a level
order traversal, where '#' signifies a path terminator where no node
exists below. Here's an example:1    / \   2   3      /     4      \
5The above binary tree is serialized as"{1,2,3,#,#,4,#,#,5}".

Tags: Tree, Breadth-first Search, Stack
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
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        curr_level = [root]
        ret = []
        while curr_level:
            next_level = []
            if len(ret) % 2 == 0:
                for node in reversed(curr_level):
                    next_level.append(node.right)
                    next_level.append(node.left)
                ret.append([node.val for node in curr_level])
            else:
                for node in reversed(curr_level):
                    next_level.append(node.left)
                    next_level.append(node.right)
                ret.append([node.val for node in curr_level])
            curr_level = filter(lambda x: x is not None, next_level)
        return ret

s = Solution()
t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
t.left.left = TreeNode(4)
t.left.right = TreeNode(5)

for item in s.zigzagLevelOrder(t):
    print item