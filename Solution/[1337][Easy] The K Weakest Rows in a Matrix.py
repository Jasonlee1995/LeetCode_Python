class Solution:
    def kWeakestRows(self, mat, k):
        sorted_idx = sorted(range(len(mat)), key=lambda i: (sum(mat[i]), i))
        return sorted_idx[:k]