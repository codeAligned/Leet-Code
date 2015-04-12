'''
P-100 - Same Tree

Given two binary trees, write a function to check if they are equal or
not. Two binary trees are considered equal if they are structurally
identical and the nodes have the same value.

Tags: Tree, Depth-first Search
'''

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean

    # Iterative DFS solution
    def isSameTree(self, p, q):
        # check if any of p or q is None
        if not q or not p:
            return q == p
            
        ps, qs = [p, ], [q, ]
        while ps and qs:
            pp, pq = ps.pop(), qs.pop()
            if pp.val != pq.val:
                return False
            if pp.left and pq.left:
                ps.append(pp.left)
                qs.append(pq.left)
            elif pp.left or pq.left:
                return False
            if pp.right and pq.right:
                ps.append(pp.right)
                qs.append(pq.right)
            elif pp.right or pq.right:
                return False
        return True if not ps and not qs else False

t1 = TreeNode(1)
#t1.left = TreeNode(3)
t1.right = TreeNode(2)

t2 = TreeNode(1)
t2.right = TreeNode(2)

s = Solution()
print s.isSameTree(t1, t2)