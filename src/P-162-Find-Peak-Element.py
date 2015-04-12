'''
P-162 - Find Peak Element

A peak element is an element that is greater than its neighbors. Given
an input array wherenum[i]  num[i+1], find a peak element and return
its index. The array may contain multiple peaks, in that case return
the index to any one of the peaks is fine. You may imagine thatnum[-1]
= num[n] = -. For example, in array[1, 2, 3, 1], 3 is a peak element
and your function should return the index number 2. click to show
spoilers. Your solution should be in logarithmic complexity.
Credits:Special thanks to@tsfor adding this problem and creating all
test cases.

Tags: Array, Binary Search
'''

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