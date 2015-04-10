class Solution:
    # @param num, a list of integer
    # @return an integer
    # iterative
    def bin_search(self, A, i, j):
        lo, hi = i, j
        while lo < hi:
            mid = (lo + hi) / 2
            if A[mid] > A[hi]:
                lo = mid + 1
            elif A[mid] < A[hi]:
                hi = mid
            elif A[mid] == A[lo]:
                lo += 1
                hi -= 1
            else:
                hi = mid
        return lo

    def findMin(self, num):
        return num[self.bin_search(num, 0, len(num) - 1)]