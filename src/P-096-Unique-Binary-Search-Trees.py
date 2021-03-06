'''
P-096 - Unique Binary Search Trees

Givenn, how many structurally uniqueBST's(binary search trees) that
store values 1...n? For example,Givenn= 3, there are a total of 5
unique BST's.1         3     3      2      1      \       /     /
/ \      \       3     2     1      1   3      2      /     /       \
\     2     1         2                 3

Tags: Tree, Dynamic Programming
'''

class Solution:
    # @return an integer

    # DP-based Solution
    # m[i] means the number of unique BST's with i nodes
    def numTrees(self, n):
        m = [0] * (n + 1)
        m[0] = m[1] = 1
        for k in range(2, n + 1):
            for i in range(1, k + 1):
                m[k] += m[i - 1] * m[k - i]
        return m[n]

s = Solution()
print s.numTrees(3)