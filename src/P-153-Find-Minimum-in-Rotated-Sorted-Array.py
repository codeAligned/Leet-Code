class Solution:
    # @param num, a list of integer
    # @return an integer

    # recursive
    def bin_search(self, A, i, j):
        m = (i + j) / 2
        if not i < j:
            return i
        elif A[m] > A[j]:
            # min is on the right side
            return self.search(A, m + 1, j)
        else:
            # min is on the left side - include m
            return self.search(A, i, m)

    # iterative
    def bin_search(self, A, i, j):
        lo, hi = i, j
        while lo < hi:
            mid = (lo + hi) / 2
            if A[mid] > A[hi]:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def findMin(self, num):
        return num[self.bin_search(num, 0, len(num) - 1)]

s = Solution()
l = [
    [1],
    [2, 1],
    [1, 2],
    [1, 2, 3],
    [3, 1, 2],
    [2, 3, 1],
    [1, 2, 3, 4],
    [2, 3, 4, 1],
    [3, 4, 1, 2],
    [4, 1, 2, 3],
]
for item in l:
    print s.findMin(item)