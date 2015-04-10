class Solution:
    # @param s, a string
    # @return a boolean

    # O(len(s)) space complexity
    def isPalindrome(self, s):
        s = ''.join([c.lower() for c in s if c.isalnum()])
        for i in range(len(s) / 2):
            if s[i] != s[len(s) - i - 1]:
                return False
        return True

    # O(1) space complexity
    def isPalindrome(self, s):
        i, j = 0, len(s) - 1
        while i < j:
            while not s[i].isalnum() and i < j:
                i += 1
            while not s[j].isalnum() and i < j:
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True

s = Solution()
print s.isPalindrome('a ba')