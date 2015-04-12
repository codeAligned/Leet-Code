'''
P-035 - Search Insert Position

Given a sorted array and a target value, return the index if the
target is found. If not, return the index where it would be if it were
inserted in order. You may assume no duplicates in the array. Here are
few examples.[1,3,5,6], 5 &#8594; 2[1,3,5,6], 2 &#8594; 1[1,3,5,6], 7
&#8594; 4[1,3,5,6], 0 &#8594; 0

Tags: Array, Binary Search
'''

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        return self.binary_search(A, 0, len(A), target)
    
    def binary_search(self, A, i, j, target):
        if not i < j:
            return i
        if target > A[(j + i) / 2]:
            return self.binary_search(A, (j + i) / 2 + 1, j, target)
        elif target < A[(j + i) / 2]:
            return self.binary_search(A, i, (j + i) / 2, target)
        else:
            return (i + j) / 2

s = Solution()

l = [1,3,4,5,6]
print s.searchInsert(l, 2)