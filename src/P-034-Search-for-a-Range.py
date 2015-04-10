class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]

    # Use two modified binary search algorithm
    def searchRange(self, A, target):
        # Search for the left end
        l, h = 0, len(A) - 1
        while l < h:
            m = (l + h) / 2
            if A[m] < target:
                l = m + 1
            else:
                h = m
        i = l

        # Search for the right end
        h = len(A) - 1          # reset the high pointer
        while l < h:
            m = (l + h) / 2 + 1 # middle biased to the right
            if A[m] > target:
                h = m - 1
            else:
                l = m           # so that this won't stuck the search
        j = h

        # check if we found the target or not
        if A[i] == A[j] == target:
            return [i, j]
        else:
            return [-1, -1]

s = Solution()

l = [1,2,4,4,4,4,5,5,6]
print s.searchRange(l, 4)