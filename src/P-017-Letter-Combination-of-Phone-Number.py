class Solution:
    # @return a list of strings, [s1, s2]
    def __init__(self):
        self.map = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        self.output = []

    def letterCombinations(self, digits, pos = 0, string = None):
        # Initialize
        if pos == 0:
            string = []
            digits = [int(c) for c in digits if c not in '01']

        if len(string) == len(digits):
            self.output.append(''.join(string))
            return self.output

        # Recursion
        for c in self.map[digits[pos]]:
            string.append(c)
            self.letterCombinations(digits, pos + 1, string)
            string.pop()

        return self.output

s = Solution()
for i in s.letterCombinations('234'):
    print i