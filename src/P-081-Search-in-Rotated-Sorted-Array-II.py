class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean

    # One-pass Solution
    def search(self, A, target):
        l, h = 0, len(A) - 1
        while l <= h:
            m = (l + h) / 2
            # check if we found the target
            if A[m] == target:
                return True
            # left half of the list is sorted
            if A[m] > A[l]:
                # target falls in the left part
                if A[l] <= target and target < A[m]:
                    h = m - 1
                # target falls in the right part
                else:
                    l = m + 1
            # right half of the list is sorted
            elif A[m] < A[l]:
                if A[m] < target and target <= A[h]:
                    l = m + 1
                else:
                    h = m - 1
            # When duplicates are allowed and A[m] == A[l]
            # You don't know which part to go
            # The only way is to increment l
            # which decrease the search space by 1
            else:
                l += 1
        return False

s = Solution()
l = [5,1,1,1,1,1,1,1,1,1,1,1]

print s.search(l, 5)