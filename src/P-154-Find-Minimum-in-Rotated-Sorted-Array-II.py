'''
P-154 - Find Minimum in Rotated Sorted Array II

Follow upfor "Find Minimum in Rotated Sorted Array":What
ifduplicatesare allowed?Would this affect the run-time complexity? How
and why? Follow upfor "Find Minimum in Rotated Sorted Array":What
ifduplicatesare allowed? Would this affect the run-time complexity?
How and why? Suppose a sorted array is rotated at some pivot unknown
to you beforehand. (i.e.,0 1 2 4 5 6 7might become4 5 6 7 0 1 2). Find
the minimum element. The array may contain duplicates.

Tags: Array, Binary Search
'''

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