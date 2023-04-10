import itertools


class Solution:
    def minStartValue(self, nums):
        return max(1, -min(itertools.accumulate(nums)) + 1)