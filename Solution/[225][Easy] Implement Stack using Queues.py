import collections


class MyStack:
    def __init__(self):
        self.deque = collections.deque([])

    def push(self, x):
        self.deque.append(x)
        for _ in range(len(self.deque)-1):
            self.deque.append(self.deque.popleft())

    def pop(self):
        return self.deque.popleft()

    def top(self):
        return self.deque[0]

    def empty(self):
        return len(self.deque) == 0
