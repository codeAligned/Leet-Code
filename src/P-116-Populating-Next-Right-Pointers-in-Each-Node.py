'''
P-116 - Populating Next Right Pointers in Each Node

Given a binary treestruct TreeLinkNode {        TreeLinkNode *left;
TreeLinkNode *right;        TreeLinkNode *next;      } Populate each
next pointer to point to its next right node. If there is no next
right node, the next pointer should be set toNULL. Initially, all next
pointers are set toNULL. Note:You may only use constant extra
space.You may assume that it is a perfect binary tree (ie, all leaves
are at the same level, and every parent has two children). For
example,Given the following perfect binary tree,1         /  \
2    3       / \  / \      4  5  6  7 After calling your function, the
tree should look like:1 -> NULL         /  \        2 -> 3 -> NULL
/ \  / \      4->5->6->7 -> NULL

Tags: Tree, Depth-first Search
'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        while root.left:
            curr = root
            while curr:
                curr.left.next = curr.right
                # We can do this because the we have built the next pointer
                # for the upper level
                if curr.next:
                    curr.right.next = curr.next.left
                curr = curr.next
            root = root.left