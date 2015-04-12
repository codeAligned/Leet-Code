'''
P-125 - Valid Palindrome

Given a string, determine if it is a palindrome, considering only
alphanumeric characters and ignoring cases. For example,"A man, a
plan, a canal: Panama"is a palindrome."race a car"isnota palindrome.
Note:Have you consider that the string might be empty? This is a good
question to ask during an interview. For the purpose of this problem,
we define empty string as valid palindrome.

Tags: Two Pointers, String
'''

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