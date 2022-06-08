import collections


class RecentCounter:
    def __init__(self):
        self.request = collections.deque([])

    def ping(self, t):
        self.request.append(t)
        while self.request and (self.request[0] < t-3000):
            self.request.popleft()
        return len(self.request)