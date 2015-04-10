class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) == 0:
            return 0
        i, j = 0, 0
        for i in range(1, len(A)):
            if A[i] != A[j]:
                j += 1
                A[j] = A[i]
        return j + 1


s = Solution()

l = [1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3]
#l = [1,1,2]
#l=[]
l=[1]
print s.removeDuplicates(l)
print l