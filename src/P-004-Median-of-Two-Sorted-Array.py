'''
P-004 - Median of Two Sorted Arrays

There are two sorted arrays A and B of size m and n respectively. Find the
median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Tags: Divide and Conquer, Array, Binary Search
'''

class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        m, n = len(A), len(B)

        # A is always the shorter array
        if m > n:
            return self.findMedianSortedArrays(B, A)

        # Binary Search
        imin, imax = 0, m
        while imin <= imax:
            i = (imin + imax) / 2
            j = (m + n + 1) / 2  - i
            if j > 0 and i < m and B[j - 1] > A[i]:
                imin = i + 1
            elif i > 0 and j < n and A[i - 1] > B[j]:
                imax = i - 1
            else:
                if i == 0:
                    num1 = B[j - 1]
                elif j == 0:
                    num1 = A[i - 1]
                else:
                    num1 = max(A[i - 1], B[j - 1])

                # total length is odd
                if (m + n) & 1:
                    return num1

                # total length is even
                if i == m:
                    num2 = B[j]
                elif j == n:
                    num2 = A[i]
                else:
                    num2 = min(A[i], B[j])

                return (num1 + num2) / 2.0

from utils import *

cases = [
    Test_case(([2], [1, 3, 4]), 2.5),
    Test_case(([2], [4]), 3),
    Test_case(([2], [3, 4]), 3),
    Test_case(([2], [1, 3, 4, 5]), 3),
    Test_case(([2], []), 2),
    Test_case(([2, 4], []), 3),
]

run_cases(Solution().findMedianSortedArrays, cases)
