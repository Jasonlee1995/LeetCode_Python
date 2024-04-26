class Solution:
    def construct2DArray(self, original, m, n):
        if len(original) != m * n: return []
        return [original[n*idx:n*(idx+1)] for idx in range(m)]