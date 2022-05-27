class Solution:
    def smallestRangeI(self, nums, k):
        return max(0, max(nums) - min(nums) - 2 * k)