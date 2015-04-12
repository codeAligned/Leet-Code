'''
P-080 - Remove Duplicates from Sorted Array II

Follow up for "Remove Duplicates":What if duplicates are allowed at
mosttwice? For example,Given sorted array A =[1,1,1,2,2,3], Your
function should return length =5, and A is now[1,1,2,2,3].

Tags: Array, Two Pointers
'''

class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0
        prev = A[0]
        count = length = 1
        for curr in range(1, len(A)):
            if A[curr] == prev:
                if count == 2:
                    continue
                else:
                    count += 1
            else:
                prev = A[curr]
                count = 1
            A[length] = A[curr]
            length += 1
        return length

s = Solution()
l = [1,1,1,2,2,3]
print s.removeDuplicates(l), l