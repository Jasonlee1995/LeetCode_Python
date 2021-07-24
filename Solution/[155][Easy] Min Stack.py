class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        if self.stack: self.stack.append((val, min(val, self.stack[-1][1])))
        else: self.stack.append((val, val))

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1][0]

    def getMin(self):
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
