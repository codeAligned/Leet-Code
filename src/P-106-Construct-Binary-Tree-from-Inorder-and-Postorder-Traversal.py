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
        m = self.inorder.index(self.postorder[j - 1])
        left_size = m - x
        node = TreeNode(self.postorder[j - 1])
        node.left = self.build(i, i + left_size, x, m)
        node.right = self.build(i + left_size, j - 1, m + 1, y)
        return node

    def buildTree(self, inorder, postorder):
        self.postorder = postorder
        self.inorder = inorder
        if not postorder:
            return None
        return self.build(0, len(postorder), 0, len(inorder))

    # Iterative Solution
    def buildTree(self, inorder, postorder):
        if not postorder:
            return None
        pre_ptr, in_ptr = len(postorder) - 2, len(inorder) - 1
        root = TreeNode(postorder[-1])
        stack = [root]
        
        while True:
            if inorder[in_ptr] == stack[-1].val:
                node = stack.pop()
                in_ptr -= 1
                if in_ptr == -1:
                    break
                if stack and inorder[in_ptr] == stack[-1].val:
                    continue
                node.left = TreeNode(postorder[pre_ptr])
                pre_ptr -= 1
                stack.append(node.left)
            else:
                node = TreeNode(postorder[pre_ptr])
                pre_ptr -= 1
                stack[-1].right = node
                stack.append(node)
        return root