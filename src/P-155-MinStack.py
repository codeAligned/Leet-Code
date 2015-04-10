class MinStack:
    # @param x, an integer
    # @return an integer
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        self.stack.append(x)
        if len(self.min_stack) == 0 or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    # @return nothing
    def pop(self):
        if len(self.stack) > 0:
            x = self.stack.pop()
            if x == self.min_stack[-1]:
                self.min_stack.pop()

    # @return an integer
    def top(self):
        return self.stack[-1]

    # @return an integer
    def getMin(self):
        return self.min_stack[-1]

s = MinStack()

s.push(0)
print s.top(), s.getMin()
s.push(1)
print s.top(), s.getMin()
s.push(0)
print s.top(), s.getMin()
s.pop()
print s.top(), s.getMin()
s.pop()
print s.top(), s.getMin()
s.pop()
