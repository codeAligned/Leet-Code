class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        m = {}
        if len(num) == 1:
            return num[0]
        for c in num:
            if c in m:
                m[c] += 1
                if m[c] > len(num) / 2:
                    return c
            else:
                m[c] = 1

s = Solution()
print s.majorityElement([1,])