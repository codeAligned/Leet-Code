'''
P-041 - First Missing Positive

Given an unsorted integer array, find the first missing positive
integer. For example,Given[1,2,0]return3,and[3,4,-1,1]return2. Your
algorithm should run inO(n) time and uses constant space.

Tags: Array
'''

class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        i = 0
        j = len(A)-1
        while (i <= j):
            if A[i] > j+1 or A[i] <= 0 or (A[i] == A[A[i]-1] and i != A[i]-1):
                A[i] = A[j]
                j -= 1
            elif i == A[i]-1:
                i += 1
                continue
            else:
                A[A[i]-1], A[i] = A[i], A[A[i]-1]
        return i+1