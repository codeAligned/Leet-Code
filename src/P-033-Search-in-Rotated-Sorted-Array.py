'''
P-033 - Search in Rotated Sorted Array

Suppose a sorted array is rotated at some pivot unknown to you
beforehand. (i.e.,0 1 2 4 5 6 7might become4 5 6 7 0 1 2). You are
given a target value to search. If found in the array return its
index, otherwise return -1. You may assume no duplicate exists in the
array.

Tags: Array, Binary Search
'''

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer

    # Two-pass solution
    # First Find out the offset of the array
    # which is the position of the minimum
    # Then use the offset and perform a normal binary search
    def search(self, A, target):
        lo, hi, n = 0, len(A) - 1, len(A)
        while lo < hi:
            mid = (lo + hi) / 2
            if A[mid] > A[hi]:
                lo = mid + 1
            else:
                hi = mid
        shift, lo, hi = lo, 0, n - 1
        
        while lo <= hi:
            mid = (lo + hi) / 2
            mid_shifted = (mid + shift) % n
            if A[mid_shifted] < target:
                lo = mid + 1
            elif A[mid_shifted] > target:
                hi = mid - 1
            else:
                return mid_shifted
        return -1

    # One-pass solution
    def search(self, A, target):
        l, h = 0, len(A) - 1
        while l < h:
            m = (l + h) / 2
            # check if we found the target
            if A[m] == target:
                return mid
            # left half of the list is sorted
            if A[m] >= A[l]:
                # target falls in the left part
                if A[l] <= target and target < A[m]:
                    h = m - 1
                # target falls in the right part
                else:
                    l = m + 1
            # right half of the list is sorted
            else:
                if A[m] < target and target <= A[h]:
                    l = m + 1
                else:
                    h = m - 1
        return l if A[l] == target else -1

s = Solution()
l = [4,5,6,7,0,1,2]
l = [0,1,2,4,5,6,7]

for i in l:
    print s.search(l, i)
print s.search(l, 99)