class Solution:
    def arrayRankTransform(self, arr):
        num2idx = {}
        for idx, num in enumerate(sorted(set(arr))):
            num2idx[num] = idx+1
        return [num2idx[num] for num in arr]