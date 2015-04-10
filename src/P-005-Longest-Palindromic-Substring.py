class Solution:
    # @return a string

    # Straightforward
    # O(n ^ 2)
    def longestPalindrome(self, s):
        self.s = s
        ms = ml = 0
        for k in range(len(s)):
            # Odd length
            if self.is_palindrome(k - ml, k):
                ms = k - ml
                ml += 1
            # Even length
            elif k - ml - 1 >= 0 and self.is_palindrome(k - ml - 1, k):
                ms = k - ml - 1
                ml += 2
        return s[ms : ms + ml]

    def is_palindrome(self, start, end):
        for i in xrange((end - start + 1) / 2):
            if self.s[start + i] != self.s[end - i]:
                return False
        return True

    # Manacher's Algorithm
    # O(n) Time
    def preProcess(self, s):
        if len(s) == 0:
            return "^$"
        ret = "^"
        for c in s:
            ret += '#' + c
        ret += "#$"
        return ret

    def longestPalindrome(self, s):
        T = self.preProcess(s)
        P = [0] * len(T)
        C, R = 0, 0
        for i in range(1, len(T) - 1):
            i_mirror = 2 * C - i 
            P[i] = min(R - i, P[i_mirror]) if (R > i) else 0
            
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1

            if i + P[i] > R:
                C = i
                R = i + P[i]

        length = max(P)
        index = P.index(length)

        return s[(index - 1 - length)/2 : (index - 1 + length)/2]

s = Solution()

print s.longestPalindrome('12343252311325')
print s.longestPalindrome('')
print s.longestPalindrome('1')
print s.longestPalindrome('11')
print s.longestPalindrome('131')
print s.longestPalindrome('123215')
print s.longestPalindrome('41441')