class Solution:
    # @return a boolean
    def isValid(self, s):
        p = {'(':')', '[':']', '{':'}',}
        stack = []
        for c in s:
            if c in p.keys():
                stack.append(c)
            elif c in p.values() and (len(stack) == 0 or p[stack.pop()] != c):
                return False
        return len(stack) == 0

s = Solution()

print s.isValid('{[()]}')
print s.isValid('')
print s.isValid('[}')
print s.isValid('[[][[[}')
print s.isValid('[[][[[]')