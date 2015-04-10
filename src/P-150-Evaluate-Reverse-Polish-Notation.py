class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        stack = []
        opercode = set(['+', '/', '*', '-'])
        for token in tokens:
            if not token in opercode:
                stack.append(int(token))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                # because the way Python round numbers
                stack.append(int(eval('float(op1)' + token + 'op2')))
            #print token, stack
        return stack.pop()

s = Solution()
l = ["2", "1", "+", "3", "*"]
l = ["4", "13", "5", "/", "+"]
l = ["3", "-4", "+"]
l = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print s.evalRPN(l)