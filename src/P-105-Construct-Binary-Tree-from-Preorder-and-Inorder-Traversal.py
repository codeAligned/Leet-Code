# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node

    # Recursive Solution
    def build(self, i, j, x, y):
        if not i < j:
            return None
        m = self.inorder.index(self.preorder[i])
        left_size = m - x
        node = TreeNode(self.preorder[i])
        node.left = self.build(i + 1, i + 1 + left_size, x, m)
        node.right = self.build(i + 1 + left_size, j, m + 1, y)
        return node

    def buildTree(self, preorder, inorder):
        self.preorder = preorder
        self.inorder = inorder
        if not preorder:
            return None
        return self.build(0, len(preorder), 0, len(preorder))

    # Iterative Solution
    def buildTree(self, preorder, inorder):
        if not preorder:
            return None
        pre_ptr, in_ptr = 1, 0
        root = TreeNode(preorder[0])
        stack = [root]
        
        while True:
            if inorder[in_ptr] == stack[-1].val:
                node = stack.pop()
                in_ptr += 1
                if in_ptr == len(inorder):
                    break
                if stack and inorder[in_ptr] == stack[-1].val:
                    continue
                node.right = TreeNode(preorder[pre_ptr])
                pre_ptr += 1
                stack.append(node.right)
            else:
                node = TreeNode(preorder[pre_ptr])
                pre_ptr += 1
                stack[-1].left = node
                stack.append(node)
        return root