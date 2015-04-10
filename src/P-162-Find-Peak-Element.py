class Solution:
    # @param num, a list of integer
    # @return an integer
    def aux(self, i, j):
        if not i < j:
            return i
        m = (i + j) / 2
        if self.num[m] > self.num[m + 1]:
            return self.aux(i, m)
        else:
            return self.aux(m + 1, j)

    def findPeakElement(self, num):
        self.num = num
        return self.aux(0, len(num) - 1)


s = Solution()
l = [1,2,3]
l = [1,3,2]
l = [3,2,1]
l = [1,2,3,4,5,2,1]
l = [2,1]
l = [1,2]

try:
    print s.findPeakElement(l)
except RuntimeError:
    print 'runtime error'