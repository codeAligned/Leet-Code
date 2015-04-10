class Solution:
    # @return a tuple, (index1, index2)

    # Hashmap-based Solution
    # O(n) Time O(n) Space
    def twoSum(self, num, target):
        m = {}
        for i, n in enumerate(num):
            if n not in m:
                m[n] = [i + 1, ]
            else:
                m[n].append(i + 1)
        for n1 in num:
            n2 = target - n1
            if n2 == n1:
                if len(m[n1]) != 1:
                    return min(m[n1]), max(m[n1])
            elif n2 in m:
                return min(m[n2][0], m[n1][0]), max(m[n2][0], m[n1][0])

    # Two-pointer-based Solution
    # O(n) Time O(n) Space
    def twoSum(self, num, target):
        m = sorted(enumerate(num), key = lambda x : x[1])
        i, j = 0, len(m) - 1
        while i < j:
            n = m[i][1] + m[j][1]
            if target > n:
                i += 1
            elif target < n:
                j -= 1
            else:
                return (min(m[i][0] + 1, m[j][0] + 1), 
                        max(m[i][0] + 1, m[j][0] + 1))

# Testing
from utils import *

cases = [
	Test_case(([1, 2], 3), (1, 2)),
	Test_case(([1, 2, 3], 3), (1, 2)),
]

print run_cases(Solution().twoSum, cases)