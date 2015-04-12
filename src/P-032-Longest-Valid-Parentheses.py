'''
P-032 - Longest Valid Parentheses

Given a string containing just the characters'('and')', find the
length of the longest valid (well-formed) parentheses substring.
For"(()", the longest valid parentheses substring is"()", which has
length = 2. Another example is")()())", where the longest valid
parentheses substring is"()()", which has length = 4.

Tags: Dynamic Programming, String
'''

class Solution:
    # @param s, a string
    # @return an integer

    # DP-based Solution
    # V[i] is the number of valid parentheses till i
    def longestValidParentheses(self, s):
        V = [0] * (len(s) + 1) # +1 in case s is empty so that the last return won't cause error
        open_count = 0
        for i, c in enumerate(s):
            if c == '(':
                open_count += 1
            if c == ')' and open_count > 0:
                V[i] = 2 + V[i - 1]
                if i - V[i] > 0:
                    V[i] += V[i - V[i]]
                open_count -= 1
        return max(V)

    # Stack-based Solution
    def longestValidParentheses(self, s):
        stack = []
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                else:
                    stack.append(i)
        # Elements left in the stack are those cannot be matched
        # Add two guard
        stack.insert(0, -1)
        stack.append(len(s))
        # Find the maximum interval betwen adjacent indices in the stack
        return max(stack[i + 1] - stack[i] - 1 for i in range(len(stack) - 1))

s = Solution()
print s.longestValidParentheses("()()()()")