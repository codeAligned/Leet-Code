class Solution:
    # @return a boolean
    def num_digits(self, x):
        i = 0
        while x > 0:
            x = x / 10
            i += 1
        return i

    def kth_digit(self, x, k):
        return (x % 10 ** (k + 1)) / 10 ** k

    def isPalindrome(self, x):
        if x < 0:
            return False
        i = self.num_digits(x)
        flag = True
        if i == 1:
            return True
        for k in range(0, i / 2):
            if self.kth_digit(x, k) == self.kth_digit(x, i - k - 1):
                continue
            else:
                flag = False
                break
        return flag

    def isPalindrome(self, x):
        if x % 10 == 0 and x != 0 or x < 0:
            return False
        i = 0
        while i < x:
            i = i * 10 + x % 10
            x = x / 10
        return i == x or i / 10 == x

s = Solution()

print s.isPalindrome(123321)
print s.isPalindrome(12321)
print s.isPalindrome(-123321)
print s.isPalindrome(-12321)
print s.isPalindrome(-123521)
