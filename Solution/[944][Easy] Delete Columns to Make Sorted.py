class Solution:
    def minDeletionSize(self, strs):
        return sum(list(c) != sorted(c) for c in zip(*strs))