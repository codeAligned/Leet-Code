# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a list node
    # @return a tree node

    # Recursive DFS solution
    def aux(self, i, j):
        if i == j:
            return self.l[i]
        if i > j:
            return None
        m = (i + j) / 2
        self.l[m].left = self.aux(i, m - 1) 
        self.l[m].right = self.aux(m + 1, j)
        return self.l[m]

    def sortedArrayToBST(self, num):
        # Convert the linked list to a list of treenode
        # Because its a height-balanced tree, we can always choose the 
        # middle to be the root
        self.l = [TreeNode(n) for n in num]
        return self.aux(0, len(self.l) - 1)

s = Solution()