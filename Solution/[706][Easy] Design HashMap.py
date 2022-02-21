class MyHashMap:
    def __init__(self):
        self.size = 10**4
        self.buckets = [[] for _ in range(self.size)]

    def put(self, key, value):
        bucket, idx = self._index(key)
        if idx != -1: bucket[idx] = (key, value)
        else: bucket.append((key, value))

    def get(self, key):
        bucket, idx = self._index(key)
        if idx != -1: return bucket[idx][1]
        else: return -1

    def remove(self, key):
        bucket, idx = self._index(key)
        if idx != -1: bucket.pop(idx)

    def _hash(self, key):
        return key % self.size

    def _index(self, key):
        hash_ = self._hash(key)
        bucket = self.buckets[hash_]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                return bucket, i
        return bucket, -1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
