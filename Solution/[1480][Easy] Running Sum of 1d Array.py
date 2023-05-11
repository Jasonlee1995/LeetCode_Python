import itertools


class Solution:
    def runningSum(self, nums):
        return itertools.accumulate(nums)