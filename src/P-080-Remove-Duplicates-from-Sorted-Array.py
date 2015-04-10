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