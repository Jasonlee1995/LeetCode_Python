class Solution:
    def singleNumber(self, nums):
        return 2*sum(set(nums)) - sum(nums)
