class Solution:
    def maxCount(self, m, n, ops):
        if not ops: return m * n
        m, n = zip(*ops)
        return min(m) * min(n)
