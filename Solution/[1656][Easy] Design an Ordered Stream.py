class OrderedStream:
    def __init__(self, n):
        self.data = [None] * n
        self.ptr = 0

    def insert(self, idKey, value):
        idx = idKey - 1
        self.data[idx] = value
        
        answer = []
        if idx == self.ptr:
            for i in range(idx, len(self.data)):
                if self.data[i] == None:
                    self.ptr = i
                    break
                answer.append(self.data[i])
        return answer


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)