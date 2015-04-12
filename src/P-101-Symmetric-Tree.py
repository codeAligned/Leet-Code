'''
P-101 - Symmetric Tree

Given a binary tree, check whether it is a mirror of itself (ie,
symmetric around its center). For example, this binary tree is
symmetric:1     / \    2   2   / \ / \  3  4 4  3 But the following is
not:1     / \    2   2     \   \     3    3 Note:Bonus points if you
could solve it both recursively and iteratively. confused
what"{1,#,2,3}"means?> read more on how binary tree is serialized on
OJ. The serialization of a binary tree follows a level order
traversal, where '#' signifies a path terminator where no node exists
below. Here's an example:1    / \   2   3      /     4      \
5The above binary tree is serialized as"{1,2,3,#,#,4,#,#,5}".

Tags: Tree, Depth-first Search
'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean

    # Recursive solution
    def aux(self, left, right):
        # If any of the left or right is None
        # check if the other one is None also.
        if not left or not right:
            return left == right
        # left and right need to have same value
        # the left of left should be the same with the right of the right
        # the right of left should be the same with the left of the right
        return left.val == right.val and                \
                self.aux(left.left, right.right) and    \
                self.aux(left.right, right.left)

    def isSymmetric(self, root):
        return not root or self.aux(root.left, root.right)