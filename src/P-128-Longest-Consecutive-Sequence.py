from collections import defaultdict

class Solution:
    # @param num, a list of integer
    # @return an integer

    # Store the length of the sequence at its two ends
    def longestConsecutive(self, num):
        m = defaultdict(lambda:0)
        max_len = 0
        for n in num:
            if m[n] == 0:
                m[n] = m[n + m[n + 1]]          \
                     = m[n - m[n - 1]]          \
                     = m[n + 1] + m[n - 1] + 1
                max_len = max(max_len, m[n])
            #print n, max_len, m
        return max_len

s = Solution()
n = [100, 4, 200, 1, 3, 2]
n = [1, 2, 0, 1]
n = [0, 3, 2,]
print s.longestConsecutive(n)