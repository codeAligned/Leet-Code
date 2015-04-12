'''
P-117 - Populating Next Right Pointers in Each Node II

Follow up for problem "Populating Next Right Pointers in Each Node".
What if the given tree could be any binary tree? Would your previous
solution still work? Note:You may only use constant extra space. For
example,Given the following binary tree,1         /  \        2    3
/ \    \      4   5    7 After calling your function, the tree should
look like:1 -> NULL         /  \        2 -> 3 -> NULL       / \    \
4-> 5 -> 7 -> NULL

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

    # Level-order traversal
    def connect(self, root):
        # Current node of current level
        curr = root
        # Head of the next level
        head = None
        # The leading node on the next level
        prev = None
        while curr:
            # Iterate on the current level
            while curr:
                # Left child
                if curr.left:
                    if prev:
                        prev.next = curr.left
                    else:
                        head = curr.left
                    prev = curr.left
                # Right child
                if curr.right:
                    if prev:
                        prev.next = curr.right
                    else:
                        head = curr.right
                    prev = curr.right
                # Move to next node
                curr = curr.next
            # Move to next level
            curr = head
            head = prev = None