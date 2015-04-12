'''
P-173 - Binary Search Tree Iterator

Implement an iterator over a binary search tree (BST). Your iterator
will be initialized with the root node of a BST. Callingnext()will
return the next smallest number in the BST.
Note:next()andhasNext()should run in average O(1) time and uses O(h)
memory, wherehis the height of the tree. Credits:Special thanks
to@tsfor adding this problem and creating all test cases.

Tags: Tree, Stack
'''

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# iterate through a binary search tree
# is to do in-order-traversal
# we can use iterative approach
class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack = []
        if root:
            self.stack.append(root)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return len(self.stack) > 0

    # @return an integer, the next smallest number
    def next(self):
        node = self.stack.pop()
        if hasattr(node, 'visited'):
            return node.val
        else:
            node.visited = True
            if node.right:
                self.stack.append(node.right)
            self.stack.append(node)
            if node.left:
                self.stack.append(node.left)
            return self.next()

t = TreeNode(6)
t.left = TreeNode(3)
t.right = TreeNode(10)
t.left.left = TreeNode(2)
t.left.right = TreeNode(4)
t.left.left.left = TreeNode(1)
t.left.right.right = TreeNode(5)
t.right.left = TreeNode(8)
t.right.left.right = TreeNode(9)

# Your BSTIterator will be called like this:
i, v = BSTIterator(t), []
while i.hasNext(): 
    v.append(i.next())
print v

