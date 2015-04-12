'''
P-027 - Remove Element

Given an array and a value, remove all instances of that value in
place and return the new length. The order of elements can be changed.
It doesn't matter what you leave beyond the new length.

Tags: Array, Two Pointers
'''

class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        j = 0
        for i in range(len(A)):
            if A[i] != elem:
                A[j] = A[i]
                j += 1
        return j

s = Solution()

l = [1,3,3,3,3,3,3,3,4,2,5,]
#l=[3,]
#l = []
print s.removeElement(l, 3)
print l