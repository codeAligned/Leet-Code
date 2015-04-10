class Solution:
    # @param s, a string
    # @return a list of lists of string
    def __init__(self):
        self.ret = []

    def is_palindrome(self, s):
        for i in range(len(s) / 2):
            if s[i] != s[len(s) - i - 1]:
                return False
        return True

    # Backtracking solution
    def partition(self, s, string = [], l = 0):
        if l == len(s):
            self.ret.append(string[:])

        for i in range(l + 1, len(s) + 1):
            if self.is_palindrome(s[l:i]):
                string.append(s[l:i])
                self.partition(s, string, i)
                string.pop()

        return self.ret

s = Solution()
S = 'aab'
for item in s.partition(S):
    print item