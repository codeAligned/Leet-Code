# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean

    # Use a array to store all the values and check
    # if every inserted element is in sorted order
    def in_order(self, node):
        is_valid = True
        if node.left:
            is_valid &= self.in_order(node.left)
        if not self.val_list or self.val_list[-1] < node.val:
            self.val_list.append(node.val)
        else:
            return False
        if node.right:
            is_valid &= self.in_order(node.right)
        return is_valid

    # Simpler version without a array but relies on maxint
    def in_order(self, node, max_val, min_val):
        if not node:
            return True:
        else:
            if node.val >= max_val or node.val <= min_val:
                return False
            return self.in_order(node.left, node.val, min_val)  \
                    and self.in_order(node.right, max_val, node.val)

    def isValidBST(self, root):
        self.val_list = []
        if not root:
            return True
        #return self.in_order(root)
        from sys import maxint
        return self.in_order(root, maxint, -maxint)

s = Solution()
'''
t = TreeNode(10)
t.left = TreeNode(5)
t.right = TreeNode(15)
t.right.left = TreeNode(6)
t.right.right = TreeNode(20)
'''
t = TreeNode(-2147483648)
t.right = TreeNode(2147483647)
t.right.left = TreeNode(-2147483648)

print s.isValidBST(t)