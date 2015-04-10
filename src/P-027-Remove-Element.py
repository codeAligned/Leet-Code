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