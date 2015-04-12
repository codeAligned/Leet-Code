'''
P-088 - Merge Sorted Array

Given two sorted integer arrays A and B, merge B into A as one sorted
array. Note:You may assume that A has enough space (size that is
greater or equal tom+n) to hold additional elements from B. The number
of elements initialized in A and B aremandnrespectively.

Tags: Array, Two Pointers
'''

class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing

    # O(mn) Solution given O(m) = O(n)
    def merge(self, A, m, B, n):
        k = 0
        for i, b in enumerate(B):
            while A[k] < b and k < m + i:
                k += 1
            A.insert(k, b)

    # Two-pointer-based O(m + n) Solution
    def merge(self, A, m, B, n):
        i, j = m - 1, n - 1
        for k in reversed(xrange(m + n)):
            if i < 0:
                A[k] = B[j]
                j -= 1
            elif j < 0:
                A[k] = A[i]
                i -= 1
            elif A[i] > B[j]:
                A[k] = A[i]
                i -= 1
            else:
                A[k] = B[j]
                j -= 1

A = [1,3,5,7,0,0,0,0,0,0,0,]
B = [2,4,6,8,10,12,14]

s = Solution()
s.merge(A, 4, B, 7)
s.merge([1], 1, [], 0)
print A