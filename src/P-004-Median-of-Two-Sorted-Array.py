class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        m, n = len(A), len(B)

        # A is always the shorter array
        if m > n:
            return findMedianSortedArrays(B, A)

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

s = Solution()

l1 = [2]
l2 = [1, 3, 4]
print s.findMedianSortedArrays(l1, l2)
