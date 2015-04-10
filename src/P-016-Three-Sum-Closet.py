class Solution:
    # @return the sum of the three integers
    # O(n ^ 2) Solution
    def threeSumClosest(self, num, target):
        num.sort()
        m = target - sum(num[:3])
        for k in range(len(num) - 2):
            i, j = k + 1, len(num) - 1
            while i < j:
                t = target - num[i] - num[j] - num[k]
                m = min(m, t, key = abs)
                if t > 0:
                    i += 1
                elif t < 0:
                    j -= 1
                else:
                    return target
        return target - m

s = Solution()
print s.threeSumClosest([0,0,0], 1)