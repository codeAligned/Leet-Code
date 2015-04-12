'''
P-179 - Largest Number

Given a list of non negative integers, arrange them such that they
form the largest number. For example, given[3, 30, 34, 5, 9], the
largest formed number is9534330. Note: The result may be very large,
so you need to return a string instead of an integer. Credits:Special
thanks to@tsfor adding this problem and creating all test cases.

Tags: Sort
'''

class Solution:
    # @param num, a list of integers
    # @return a string
    def compare(self, x, y):
        x, y = str(x), str(y)
        return int(x + y) - int(y + x)

    def largestNumber(self, num):
        num.sort(cmp = self.compare)
        s = ''.join(str(n) for n in reversed(num))
        i = 0
        while i < len(s) - 1:
            if s[i] != '0':
                break
            i += 1
        return s[i:] 


s = Solution()
l = [824, 8247]
#l = [63, 6]
#l = [12, 121]
print s.largestNumber(l)