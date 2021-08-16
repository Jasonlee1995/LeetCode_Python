class MyQueue:
    def __init__(self):
        self.stack = []
        self.idx = 0

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        self.idx += 1
        return self.stack[self.idx-1]

    def peek(self):
        return self.stack[self.idx]

    def empty(self):
        return len(self.stack[self.idx:]) == 0
