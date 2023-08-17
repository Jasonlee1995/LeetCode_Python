class Solution:
    def trimMean(self, arr):
        n = len(arr) // 20
        left = sorted(arr)[n:-n]
        return sum(left) / len(left)